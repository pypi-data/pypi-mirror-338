from typing import Union, Callable, Awaitable, Optional
import time
import json
import queue
import contextlib

import httpx
try:
    import httpx_ws
    websockets_supported = True
except:
    websockets_supported = False

from .models import *
from .exceptions import (DaisysTakeGenerateError, DaisysVoiceGenerateError,
                         DaisysTakeDeletionError, DaisysVoiceDeletionError,
                         DaisysVoiceUpdateError, DaisysCredentialsError)
from .sync_websocket import DaisysSyncSpeakWebsocketV1

class DaisysSyncSpeakClientV1:
    """Wrapper for Daisys v1 API endpoints, synchronous version."""
    def __init__(self, auth_url: str, product_url: str, email: str, password: str,
                 access_token: str, refresh_token: str):
        """
        Initialize the client object.

        Args:
            auth_url: str
            product_url: str
            email: str
            password: str,
            access_token: str
            refresh_token: str
        """
        if auth_url.endswith('/'):
            self.auth_url = auth_url
        else:
            self.auth_url = auth_url + '/'
        if product_url.endswith('/'):
            self.product_url = product_url
        else:
            self.product_url = product_url + '/'
        self.email = email
        self.password = password
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.httpx_client = httpx.Client()
        self.auto_logout = False
        self.token_callback = None

        # Cache redirects for 10 minutes
        self.redirect_cache_timeout = 60 * 10
        self.redirect_cache = dict()

    def login(self, email: Optional[str]=None, password: Optional[str]=None) -> bool:
        """Log in to the Daisys API using the provided credentials.

        If successful, nothing is returned.  An access token is stored in the client for
        use in future requests.  May raise:

          * DaisysCredentialsError: if insufficient credentials are provided.
          * httpx.HTTPStatusError(401): if credentials do not successfully authenticate.

        Args:
            email: User name for the Daisys API credentials.
            password: Password for the Daisys API credentials.

        """
        if not email:
            email = self.email
        if not password:
            password = self.password
        if not (email and password):
            raise DaisysCredentialsError()
        response = self.httpx_client.post(
            self.auth_url + 'login',
            headers={'Content-Type': 'application/json'},
            content=f'{{"email": "{email}", "password": "{password}"}}')
        response.raise_for_status()
        self.access_token = response.json()['access_token']
        self.refresh_token = response.json()['refresh_token']
        self.email = email
        self.password = password
        self.auto_logout = True
        if self.token_callback is not None:
            self.token_callback(self.access_token, self.refresh_token)
        return True

    def logout(self, refresh_token: Optional[str]=None) -> bool:
        """Log out of the Daisys API.  Revokes the refresh token and and forgets the
        access and refresh tokens.

          * httpx.HTTPStatusError(401): if credentials do not successfully authenticate.

        Note that further requests may auto-login again.

        Returns:
          bool: True if logout was successful, False if no tokens were provided to revoke.
        """
        if not refresh_token:
            refresh_token = self.refresh_token
        if not refresh_token:
            return False
        response = self.httpx_client.post(self.auth_url + 'logout',
                                          headers={'Content-Type': 'application/json'},
                                          content=json.dumps({'refresh_token': refresh_token}))
        response.raise_for_status()
        self.access_token = None
        self.refresh_token = None
        if self.token_callback is not None:
            self.token_callback(self.access_token, self.refresh_token)
        return True

    def close(self):
        """To be called when object is destroyed, to ensure any open HTTP connections are
        cleanly closed.  This is done automatically if the client was created through a
        context manager."""
        if self.auto_logout:
            self.logout()
        self.httpx_client.close()
        self.httpx_client = None

    def __del__(self):
        """Calls close() if the connection was not yet closed."""
        if self.httpx_client is not None:
            self.close()

    def login_refresh(self) -> Optional[bool]:
        """Refresh access and refresh tokens for API authorization.  This function does
        not normally need to be called explicitly, since the authorization credentials
        shall be renewed automatically when needed, however it is provided in case there
        is a need to do so explicitly by the user.

          * httpx.HTTPStatusError(401): if credentials do not successfully authenticate.

        Returns:
          Optional[bool]: True if successful, False if unsuccessful, and None if no refresh
                          token was available.

        """
        if self.access_token and self.refresh_token:
            response = self.httpx_client.post(
                self.auth_url + 'refresh', headers={'Content-Type': 'application/json',
                                                    'Authorization': f'Bearer {self.access_token}'},
                content=f'{{"refresh_token": "{self.refresh_token}"}}')
            if response.is_success and response.json()['access_token'] != self.access_token:
                self.access_token = response.json()['access_token']
                self.refresh_token = response.json()['refresh_token']
                if self.token_callback is not None:
                    self.token_callback(self.access_token, self.refresh_token)
            elif response.status_code != 401:
                response.raise_for_status()
            return response.is_success

    def _http(self, query: str, body: Optional[Union[dict,list]]=None, decode_json=True,
              cache_redirect=False, delete=False, location=False) -> Union[dict,str]:
        """Private function to perform an HTTP request on behalf of the client. Handles
        auto-login, token refresh, and redirect caching automatically."""
        headers = {'Client': 'daisys-python'}
        STAGE_CACHE, STAGE_TRY, STAGE_REFRESH, STAGE_LOGIN, STAGE_RETRY = range(5)
        if cache_redirect and query in self.redirect_cache and body is None:
            stage = STAGE_CACHE
        elif self.access_token:
            stage = STAGE_TRY
        elif self.refresh_token:
            stage = STAGE_REFRESH
        elif self.email and self.password:
            stage = STAGE_LOGIN
        else:
            raise DaisysCredentialsError()
        next_stage = stage
        redirect_count = 0
        timeout = 30
        while stage <= STAGE_RETRY:
            stage, next_stage = next_stage, next_stage + 1
            try:
                if stage == STAGE_CACHE:
                    cache_time, cache_url = self.redirect_cache[query]
                    if time.time() - cache_time < self.redirect_cache_timeout:
                        if str(cache_url).startswith(self.product_url):
                            response = self.httpx_client.get(cache_url, headers=headers, timeout=timeout)
                        else:
                            # No auth, assume pre-signed URL.
                            response = self.httpx_client.get(cache_url, timeout=timeout)
                    else:
                        del self.redirect_cache[query]
                elif stage in {STAGE_TRY, STAGE_RETRY}:
                    headers['Authorization'] = 'Bearer ' + self.access_token
                    if body:
                        if isinstance(body, list):
                            body_json = '[' + ','.join(b.json() for b in body) + ']'
                        elif isinstance(body, dict):
                            class json_encoder(json.JSONEncoder):
                                def default(self, obj):
                                    if hasattr(obj, 'model_dump'):
                                        return obj.model_dump()
                                    return super().default(obj)
                            body_json = json.dumps(body, cls=json_encoder)
                        else:
                            body_json = body.json()
                        headers['Content-Type'] = 'application/json'
                        response = self.httpx_client.post(self.product_url + query, headers=headers,
                                                          content=body_json, timeout=timeout)
                    elif delete:
                        response = self.httpx_client.delete(self.product_url + query, headers=headers, timeout=timeout)
                    else:
                        response = self.httpx_client.get(self.product_url + query, headers=headers, timeout=timeout)
                    while response.is_redirect and redirect_count < 10:
                        if location:
                            return str(response.next_request.url)
                        redirect_count += 1
                        try:
                            if 'X-Amz-Signature' in str(response.next_request.url):
                                # Pre-signed URL, no auth needed.
                                headers = {}
                                # We cache these, since they are good for 10 minutes.
                                self.redirect_cache[query] = time.time(), response.next_request.url

                            # Wait at least 5 minutes: since this might be a streaming
                            # URL, we just want to block until the take starts streaming.
                            response = self.httpx_client.get(response.next_request.url,
                                                             headers=headers, timeout=5*60)
                        except (httpx.ReadTimeout, httpx.ConnectTimeout):
                            # On timeout, try again, simple linear back-off schedule.
                            time.sleep(redirect_count)
                    response.raise_for_status()
                elif stage == STAGE_REFRESH:
                    if self.login_refresh():
                        next_stage = STAGE_RETRY
                    # Otherwise try login with password, so continue to next stage
                    continue
                elif stage == STAGE_LOGIN:
                    if self.email and self.password:
                        self.login(self.email, self.password)
                    continue
            except httpx.HTTPStatusError as e:
                if e.response.status_code == 401:
                    if stage < STAGE_LOGIN:
                        continue
                    else:
                        raise
                else:
                    raise
            else:
                if decode_json:
                    return response.json()
                else:
                    return response.content

    def version(self) -> Version:
        """Get the version information for the API in use.

        Returns:
            Version: An object containing version information.
        """
        response = self.httpx_client.get(self.product_url + 'version', timeout=30)
        response.raise_for_status()
        return Version(**response.json())

    def get_voice(self, voice_id: str) -> VoiceInfo:
        """Get information about a voice.

        Args:
            voice_id: The unique identififer for a voice.

        Returns:
            VoiceInfo: Information about the voice.
        """
        return VoiceInfo(**self._http('voices/' + voice_id))

    def get_voices(self, length: Optional[int]=None, page: Optional[int]=None,
                   older: Optional[int]=None, newer: Optional[int]=None) -> list[VoiceInfo]:
        """Get a list of voices, optionally filtered.

        Args:
            length:    Maximum number of voices to return.  Default: unlimited.
            page:      Return page "page" of length "length".  Default: 1.
            older:     Find voices older than or equal to this timestamp (milliseconds).
            newer:     Find voices newer than or equal to this timestamp (milliseconds).

        Returns:
            list[VoiceInfo]: Information about each voice found.
        """
        params = []
        if length:    params.append(f'length={length}')
        if page:      params.append(f'page={page}')
        if older:     params.append(f'older={older}')
        if newer:     params.append(f'newer={newer}')
        return [VoiceInfo(**r) for r in self._http('?'.join(['voices', '&'.join(params)]))]

    def get_model(self, model_name: str) -> TTSModel:
        """Get information about a model.

        Args:
            model_name: The name of the model, which is a unique identifier.

        Returns:
            TTSModel: Information about the model.
        """
        return TTSModel(**self._http('models/' + model_name))

    def get_models(self) -> list[TTSModel]:
        """Get information about all available models.

        Returns:
            list[TTSModel]: Information about each model.
        """
        return [TTSModel(**m) for m in self._http('models')]

    def generate_voice(self,
                       name: str,
                       model: str,
                       gender: VoiceGender,
                       description: Optional[str]=None,
                       default_style: Optional[list[str]]=None,
                       default_prosody: Optional[ProsodyFeaturesUnion]=None,
                       example_take: Optional[TakeGenerateWithoutVoice]=None,
                       done_webhook: Optional[str]=None,
                       wait: bool=True,
                       raise_on_error: bool=True,
                       timeout: Optional[float]=None,
                       ) -> VoiceInfo:
        """Generate a random, novel voice for a given model with desired properties.

        Args:
            name: A name to give the voice, may be any string, and does not need to be unique.
            model: The name of the model for this voice.
            gender: The gender of this voice.
            description: The description of this voice.
            default_style: An optional list of styles to associate with this voice by
                           default.  It can be overriden by a take that uses this voice.
                           Note that most styles are mutually exclusive, and not all
                           models support styles.
            default_prosody: An optional default prosody to associate with this voice.  It
                             can be overridden by a take that uses this voice.
            example_take: Information on the take to generate as an example of this voice.
            done_webhook: An optional URL to call exactly once using POST when the voice
                          is available, with VoiceInfo in the body content.

            wait: True to wait for the result, or False to continue without waiting.

            raise_on_error: If True (default) a DaisysVoiceGenerateException error will be
                            raised if an error status is detected in one of the takes.  If
                            this behavior is not desired, set to False.

            timeout: Time limit to wait, in seconds.  Note that if timeout is specified,
                     some results may not have a "done" status (ready or error).

        Returns:
            VoiceInfo: Information about the generated voice.

        """
        params = VoiceGenerate(name=name, model=model, gender=gender,
                               description=description,
                               default_style=default_style,
                               default_prosody=default_prosody,
                               example_take=example_take,
                               done_webhook=Webhook(post_url=done_webhook) if done_webhook else None)
        result = VoiceInfo(**self._http('voices/generate', params))
        if wait:
            result = self.wait_for_voices(result.voice_id, raise_on_error=raise_on_error,
                                          timeout=timeout)
        elif raise_on_error and result.status.error():
            raise DaisysVoiceGenerateError('Voice failed to generate.', response=result)
        return result

    def get_take(self, take_id: str) -> TakeResponse:
        """Get information about a specific take.

        Args:
            take_id: Unique identifier for a take.

        Returns:
            TakeResponse: Information about the requested take.
        """
        return TakeResponse(**self._http('takes/' + take_id))

    def get_takes(self, take_ids: Optional[list[str]]=None, length: Optional[int]=None,
                  page: Optional[int]=None, older: Optional[int]=None,
                  newer: Optional[int]=None) -> list[TakeResponse]:
        """Get a list of takes, optionally filtered.

        Args:
            take_ids:  A list of specific takes to retrieve.
            length:    Maximum number of voices to return.  Default: unlimited.
            page:      Return page "page" of length "length".  Default: 1.
            older:     Find voices older than or equal to this timestamp (milliseconds).
            newer:     Find voices newer than or equal to this timestamp (milliseconds).

        Returns:
            list[TakeResponse]: Information about each take found.  Empty list if none found.
        """
        params = []
        if take_ids:  params.append('take_id=' + ','.join(take_ids))
        if length:    params.append(f'length={length}')
        if page:      params.append(f'page={page}')
        if older:     params.append(f'older={older}')
        if newer:     params.append(f'newer={newer}')
        return [TakeResponse(**r) for r in self._http('?'.join(['takes', '&'.join(params)]))]

    def get_take_audio(self, take_id: str, file: Optional[str]=None, format: str='wav') -> bytes:
        """Get audio associated with a take.

        Args:
            take_id:  A take_id to retrieve the audio for.
            file:     Optionally, the filename of a file to write, or a file stream to write to.
            format:   A supported format, must be one of 'wav', 'mp3', 'flac', 'm4a'.
                      Note: only 'wav' may be retrieved without waiting for 'ready' status.

        Returns:
            bytes:    The content of the audio file associated with the requested take.
        """

        wav = self._http(f'takes/{take_id}/{format}', decode_json=False)
        if file:
            if hasattr(file, 'write'):
                file.write(wav)
            else:
                with open(file, 'wb') as f:
                    f.write(wav)
        return wav

    def get_take_audio_url(self, take_id: str, format: str='wav') -> str:
        """Get the signed URL for audio associated with a take.  May be used to
        provide the URL to a download or streaming client that does not have the
        API access token.

        Args:
            take_id:  A take_id to retrieve the audio URL for.
            format:   A supported format, msut be one of 'wav', 'mp3', 'flac', 'm4a'.
                      Note: only 'wav' may be retrieved without waiting for 'ready' status.

        Returns:
            str: The URL that can be used to download the content of the
                 audio associated with the requested take.

        """

        url = self._http(f'takes/{take_id}/{format}', decode_json=False, location=True)
        return url

    @contextlib.contextmanager
    def stream_take_audio(self, take_id: str):
        """Stream the audio by providing an iterator over chunks of bytes.

        Args:
            take_id:  A take_id to retrieve the audio URL for.

        Returns:
            iterator: use "for" to read chunks of bytes for this take.

        """

        url = self.get_take_audio_url(take_id)
        with self.httpx_client.stream('GET', url) as stream:
            if stream.is_redirect:
                with self.httpx_client.stream('GET', stream.next_request.url) as stream:
                    yield stream.iter_bytes()
            else:
                yield stream.iter_bytes()

    def wait_for_takes(self, take_ids: Union[str, list[str]],
                       sleep_seconds=0.5,
                       callback: Optional[Callable[[Union[TakeResponse,list[TakeResponse]]], None]]=None,
                       async_callback: Optional[Callable[[Union[TakeResponse,list[TakeResponse]]],
                                                         Awaitable[None]]]=None,
                       raise_on_error: bool=True,
                       timeout: Optional[float]=None,
                       ) -> Union[TakeResponse, list[TakeResponse]]:
        """Wait for a take or list of takes to be ready.

        Args:
            take_ids: Either a single take_id, or a list of take_id to wait for at the
                      same time.  In the latter case, the function will return when all
                      take_id are done.

            sleep_seconds: The number of seconds to wait while polling the take status.

            callback: A synchronous function to call whenever the status of one of the
                      takes changes.  The argument it receives corresponds to a list of
                      all takes requested.  (A single take will also be embedded in a
                      list.)

            async_callback: An asynchronous function to call whenever the status of one of
                            the takes changes.  The argument it receives corresponds to a
                            list of all takes requested.

            raise_on_error: If True (default) a DaisysTakeGeenerateException error will be
                            raised if an error status is detected in one of the takes.  If
                            this behavior is not desired, set to False.

            timeout: Time limit to wait, in seconds.  Note that if timeout is specified,
                     some results may not have a "done" status (ready or error).

        """
        sleep_seconds = max(0.5, sleep_seconds)
        if isinstance(take_ids, list):
            get = lambda x: x
        else:
            take_ids = [take_ids]
            get = lambda x: x[0]
        endpoint = 'takes?take_id=' if len(take_ids) > 1 else 'takes/'

        result = [None for _ in take_ids]
        not_done = take_ids
        idx = {k: v for v, k in enumerate(take_ids)}
        initial_time = time.time()
        while len(not_done) > 0 and (not timeout or (time.time() - initial_time) < timeout):
            if len(not_done) > 1:
                response = [TakeResponse(**v) for v in self._http('takes?take_id='+','.join(not_done))]
            else:
                response = [TakeResponse(**self._http('takes/' + not_done[0]))]
            changed = False
            not_done = []
            for r in response:
                n = idx[r.take_id]
                changed |= not result[n] or result[n].status != r.status
                result[n] = r
                if not r.status.done():
                    not_done.append(r.take_id)
            if changed:
                if callback:
                    callback(response)
                if async_callback:
                    async_callback(response)
            if len(not_done) > 0:
                time.sleep(sleep_seconds)

        if raise_on_error and any(r.status.error() for r in result):
            raise DaisysTakeGenerateError('Take failed to generate.', response=get(result))
        return get(result)

    def wait_for_voices(self, voice_ids: Union[str, list[str]],
                        sleep_seconds: float=0.5,
                        raise_on_error: bool=True,
                        timeout: Optional[float]=None,
                        ) -> Union[VoiceInfo, list[VoiceInfo]]:
        """Wait for a voice or list of voices to be ready.

        Args:
            voice_ids: Either a single voice_id, or a list of voice_id to wait for at the
                       same time.  In the latter case, the function will return when all
                       voice_id are done.

            sleep_seconds: The number of seconds to wait while polling the voice status.

            raise_on_error: If True (default) a DaisysVoiceGeenerateException error will
                            be raised if an error status is detected in one of the voices.
                            If this behavior is not desired, set to False.

            timeout: Time limit to wait, in seconds.  Note that if timeout is specified,
                     some results may not have a "done" status (ready or error).
        """
        sleep_seconds = max(0.5, sleep_seconds)
        if isinstance(voice_ids, list):
            get = lambda x: x
        else:
            voice_ids = [voice_ids]
            get = lambda x: x[0]

        result = [None for _ in voice_ids]
        not_done = voice_ids
        idx = {k: v for v, k in enumerate(voice_ids)}
        initial_time = time.time()
        while len(not_done) > 0 and (not timeout or (time.time() - initial_time) < timeout):
            if len(not_done) > 1:
                response = [VoiceInfo(**v) for v in self._http('voices?voice_id='+','.join(not_done))]
            else:
                response = [VoiceInfo(**self._http('voices/' + not_done[0]))]
            changed = False
            not_done = []
            for v in response:
                n = idx[v.voice_id]
                changed |= not result[n] or result[n].status != v.status
                result[n] = v
                if not v.status.done():
                    not_done.append(v.voice_id)
            if len(not_done) > 0:
                time.sleep(sleep_seconds)

        if raise_on_error and any(v.status.error() for v in result):
            raise DaisysVoiceGenerateError('Voice failed to generate.', response=get(result))
        return get(result)

    def generate_take(self,
                      voice_id: str,
                      text: str,
                      override_language: Optional[str]=None,
                      style: Optional[list[str]]=None,
                      prosody: Optional[ProsodyFeaturesUnion]=None,
                      status_webhook: Optional[str]=None,
                      done_webhook: Optional[str]=None,
                      wait: bool=True,
                      raise_on_error: bool=True,
                      timeout: Optional[float]=None) -> TakeResponse:
        """Generate a "take", an audio file containing an utterance of the given text by
        the given voice.

        Args:
            voice_id: The id of the voice to be used for generating audio.  The voice is
                      attached to a specific model.

            text: The text that the voice should say.

            override_language: Normally a language classifier is used to detect the language
                               of the speech; this allows for multilingual sentences.
                               However, if the language should be enforced, it should be
                               provided here.  Currently accepted values are "nl-NL" and
                               "en-GB".

            style: A list of styles to enable when speaking.  Note that most styles are
                   mutually exclusive, so a list of 1 value should be provided.  Accepted
                   styles can be retrieved from the associated voice's VoiceInfo.styles
                   or the model's TTSModel.styles field.  Note that not all models
                   support styles, thus this can be left empty if specific styles are not
                   desired.

            prosody: The characteristics of the desired speech not determined by the voice or
                     style.  Here you can provide a SimpleProsody or most models also accept
                     the more detailed AffectProsody.

            status_webhook: An optional URL to be called using ``POST`` whenever the take's
                            status changes, with :class:`TakeResponse` in the body content.

            done_webhook: An optional URL to be called exactly once using ``POST`` when the
                          take is ``READY``, ``ERROR``, or ``TIMEOUT``, with
                          :class:`TakeResponse` in the body content.

            wait: if True, wait for take to be ready before returning.

            raise_on_error: If True (default) a DaisysTakeGeenerateException error will be
                            raised.  If this behavior is not desired, set to False.

            timeout: Time limit to wait, in seconds.  Note that if timeout is specified,
                     some results may not have a "done" status (ready or error).

        Returns:
            TakeResponse: Information about the take being generated, including status.

        """
        params = TakeGenerate(voice_id=voice_id, text=text,
                              override_language=override_language,
                              style=style, prosody=prosody,
                              status_webhook=Webhook(post_url=status_webhook) if status_webhook else None,
                              done_webhook=Webhook(post_url=done_webhook) if done_webhook else None)
        result = TakeResponse(**self._http('takes/generate', params))
        if wait:
            result = self.wait_for_takes(result.take_id, raise_on_error=raise_on_error,
                                         timeout=timeout)
        elif raise_on_error and result.status.error():
            raise DaisysTakeGenerateError('Take failed to generate.', response=result)
        return result

    def generate_takes(self, request: list[TakeGenerate], wait: bool=True,
                       raise_on_error: bool=True,
                       timeout: Optional[float]=None) -> list[TakeResponse]:
        """Generate several "takes", each corresponding to an audio file containing an
        utterance of the given text by the given voice.

        Args:
            request: a list of list[TakeGenerate] objects describing multiple take generation requests.

            wait: if True, wait for all takes to be ready before returning.

            raise_on_error: If True (default) a DaisysTakeGeenerateException error will be
                            raised.  If this behavior is not desired, set to False.

            timeout: Time limit to wait, in seconds.  Note that if timeout is specified,
                     some results may not have a "done" status (ready or error).

        Returns:
            list[TakeResponse]: a list of TakeResponse objects containing information on the generation
            status of each result.

        """
        result = [TakeResponse(**r) for r in self._http('takes/generate', request)]
        if wait:
            result = self.wait_for_takes([r.take_id for r in result],
                                         raise_on_error=raise_on_error,
                                         timeout=timeout)
        elif raise_on_error and any([r.status.error() for r in result]):
            raise DaisysTakeGenerateError('Take failed to generate.', response=result)
        return result

    def delete_take(self, take_id: str, raise_on_error: bool=True) -> bool:
        """Delete a take.  The take will no longer appear in return values from get_takes.

        Args:
            take_id: the id of a take to delete.

            raise_on_error: If True (default) a DaisysTakeDeletionException error will be
                            raised if the take was not found.  (That is, if the function
                            would have returned False.)

        Returns:
            bool: True if the take was deleted successfully, otherwise False.

        Note that HTTP exceptions may be thrown for errors other than a take not being found.

        """
        try:
            result = self._http('takes/' + take_id, delete=True)
            if result is not True and raise_on_error:
                raise DaisysTakeDeletionError(f'Take {take_id} failed to delete.')
            return result
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                if raise_on_error:
                    raise DaisysTakeDeletionError(f'Take {take_id} failed to delete: not found.')
                else:
                    return False
            raise

    def delete_voice(self, voice_id: str, raise_on_error: bool=True) -> bool:
        """Delete a voice.  The voice will no longer appear in return values from get_voices.

        Args:
            voice_id: the id of a voice to delete.

            raise_on_error: If True (default) a DaisysVoiceDeletionException error will be
                            raised if the voice was not found.  (That is, if the function
                            would have returned False.)

        Returns:
            bool: True if the voice was deleted successfully, otherwise False.

        Note that HTTP exceptions may be thrown for errors other than a voice not being found.

        """
        try:
            result = self._http('voices/' + voice_id, delete=True)
            if result is not True and raise_on_error:
                raise DaisysVoiceDeletionError(f'Voice {voice_id} failed to delete.')
            return result
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                if raise_on_error:
                    raise DaisysVoiceDeletionError(f'Voice {voice_id} failed to delete: not found.')
                else:
                    return False
            raise

    def update_voice(self, voice_id: str,
                     name: Optional[str]=None,
                     gender: Optional[VoiceGender]=None,
                     description: Optional[str]=None,
                     default_style: Optional[list[str]]=None,
                     default_prosody: Optional[ProsodyFeaturesUnion]=None,
                     raise_on_error: bool=True,
                     **_kwargs) -> bool:
        """Update a voice.

        Args:
            voice_id: the id of a voice to update.
            name: A name to give the voice, may be any string, and does not need to be unique.
            gender: The gender of this voice.
            description: The description of this voice.
            default_style: An optional list of styles to associate with this voice by
                           default.  It can be overriden by a take that uses this voice.
                           Note that most styles are mutually exclusive, and not all
                           models support styles.
            default_prosody: An optional default prosody to associate with this voice.  It
                             can be overridden by a take that uses this voice.

            raise_on_error: If True (default) a DaisysVoiceUpdateException error will be
                            raised if the voice was not found.  (That is, if the function
                            would have returned False.)

        Returns:
            bool: True if the voice was updated successfully, otherwise False.

        Note that HTTP exceptions may be thrown for errors other than a voice not being found.

        """
        try:
            result = self._http('voices/' + voice_id,
                                {k: v for k, v in {'name': name, 'gender': gender,
                                                   'description': description,
                                                   'default_style': default_style,
                                                   'default_prosody': default_prosody}
                                 .items() if v is not None})
            if result is not True and raise_on_error:
                raise DaisysVoiceUpdateError(f'Voice {voice_id} failed to update.')
            return result
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                if raise_on_error:
                    raise DaisysVoiceUpdateError(f'Voice {voice_id} failed to update: not found.')
                else:
                    return False
            raise

    def websocket_url(self, model: str=None, voice_id: str=None,
                      raise_on_error: bool=True) -> str:
        """Get a URL for connecting a websocket.  Must specify model or voice_id
        in order to indicate the principle model to be used on this connection.

        Args:
            model: the model for which we want to retrieve a websocket URL.
            voice_id: the id of a voice for which we want to retrieve a websocket URL.

            raise_on_error: If True (default) an error will be raised if the
                            voice was not found or the URL could not be
                            retrieved.

        Returns:
            str: The URL to connect a websocket to.

        """
        if voice_id:
            voice = self.get_voice(voice_id)
            model = voice.model
        assert model is not None, "A model or voice must be provided."
        result = self._http('websocket/' + model, decode_json=True)
        return result["worker_websocket_url"]

    def websocket(self, model: str=None, voice_id: str=None) -> DaisysSyncSpeakWebsocketV1:
        """Get an interface to the websocket that manages the connection, allows
        making voice generate and take generate reqeusts, and handles streaming
        the resulting audio.

        This provided interface is intended to be used in a ``with`` clause.

        Args:
            model: a websocket connection requires specifying a model or voice
            voice_id: if model is not provided, voice_id must be provided

        Returns:
            :class:`.DaisysSyncSpeakWebsocketV1`
        """
        if not websockets_supported:
            raise RuntimeError("Please install httpx_ws to have websocket support.")
        if voice_id:
            voice = self.get_voice(voice_id)
            model = voice.model
        return DaisysSyncSpeakWebsocketV1(self, model)
