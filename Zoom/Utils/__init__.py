from .decolator import *
from ..Exception import APIException
import io
import urllib.request


def get_arguments(args: dict, keys: list = None, ignores: list = None):
    ret = {}
    for ky in args:
        if ky == "self":
            continue
        if keys is not None:
            if ky not in keys:
                continue
        if ignores is not None:
            if ky in ignores:
                continue
        if args[ky] is not None:
            ret[ky] = args[ky]
    if len(ret) == 0:
        return None
    return ret


def downloader(url, token):
    args = {
        "url": url,
        "headers": {
           "Authorization": "Bearer {}".format(token)
        }
    }
    req = urllib.request.Request(**args)
    try:
        with urllib.request.urlopen(req) as res:
            content = res.read()
            headers = res.headers
            contentLength = headers["Content-Length"]
            if "Content-Type" in headers:
                contentType = headers["Content-Type"]
                if contentType == "application/octet-stream":
                    content = io.BytesIO(content)
                elif contentType == "application/json":
                    content = io.StringIO(content.decode("utf-8"))
                elif contentType == "txt;charset=UTF-8":
                    content = io.StringIO(content.decode("utf-8"))
            return content, contentLength
    except urllib.error.HTTPError as e:
        ex = APIException(e)
        raise ex
