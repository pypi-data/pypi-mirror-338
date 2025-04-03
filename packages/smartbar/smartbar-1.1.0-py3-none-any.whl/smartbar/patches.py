import os
import aiohttp

class PatchedFile:
    def __init__(self, file_obj):
        self._file = file_obj
        self._ignore = False
        self._init_size()

    def _init_size(self):
        try:
            from .smartbar import SmartBar
            instance = SmartBar._instances[-1]
            if instance and not instance._auto_total_set:
                if hasattr(self._file, 'name') and os.path.isfile(self._file.name):
                    size = os.path.getsize(self._file.name)
                    if size > 0:
                        instance.total = size
                        instance._auto_total_set = True
        except:
            pass

    def read(self, size=-1):
        data = self._file.read(size)
        if not self._ignore:
            from .smartbar import SmartBar
            SmartBar._instances[-1].add(len(data))
        return data

    def write(self, data):
        if not self._ignore:
            from .smartbar import SmartBar
            SmartBar._instances[-1].add(len(data))
        return self._file.write(data)

    def __getattr__(self, name):
        return getattr(self._file, name)

    def __enter__(self):
        self._file.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self._file.__exit__(exc_type, exc_val, exc_tb)


class PatchedResponse:
    def __init__(self, resp, chunk_size=8192):
        self._resp = resp
        self._chunk_size = chunk_size
        self._ignore = False

    def iter_content(self, chunk_size=None):
        for chunk in self._resp.iter_content(chunk_size or self._chunk_size):
            if not self._ignore:
                from .smartbar import SmartBar
                SmartBar._instances[-1].add(len(chunk))
            yield chunk

    def __getattr__(self, name):
        return getattr(self._resp, name)


class PatchedAIOHTTPResponse:
    def __init__(self, resp):
        self._resp = resp
        self._ignore = False

    async def read(self):
        data = await self._resp.read()
        if not self._ignore:
            from .smartbar import SmartBar
            SmartBar._instances[-1].add(len(data))
        return data

    async def iter_chunked(self, chunk_size=8192):
        async for chunk in self._resp.content.iter_chunked(chunk_size):
            if not self._ignore:
                from .smartbar import SmartBar
                SmartBar._instances[-1].add(len(chunk))
            yield chunk

    def __getattr__(self, name):
        return getattr(self._resp, name)


def patch_aiohttp_request():
    original_request = aiohttp.ClientSession._request

    async def patched_request(self, method, url, *args, **kwargs):
        resp = await original_request(self, method, url, *args, **kwargs)
        try:
            from .smartbar import SmartBar
            transfer_encoding = resp.headers.get("Transfer-Encoding", "").lower()
            if "chunked" in transfer_encoding:
                SmartBar._instances[-1].total = 0
            else:
                length = int(resp.headers.get("Content-Length", 0))
                if length and not SmartBar._instances[-1]._auto_total_set:
                    SmartBar._instances[-1].total = length
                    SmartBar._instances[-1]._auto_total_set = True
        except:
            pass
        from .patches import PatchedAIOHTTPResponse
        return PatchedAIOHTTPResponse(resp)

    aiohttp.ClientSession._request = patched_request