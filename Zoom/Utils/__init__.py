from .decolator import *
from ..Exception import APIException
import io
import urllib.request


def get_arguments(args: dict):
    ret = {}
    for ky in args:
        if ky == "self":
            continue
        if args[ky] is not None:
            ret[ky] = args[ky]
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
            if "Content-Type" in headers:
                contentType = headers["Content-Type"]
                if contentType == "application/octet-stream":
                    content = io.BytesIO(content)
                elif contentType == "application/json":
                    content = content.decode("utf-8")
            return content
    except urllib.error.HTTPError as e:
        ex = APIException(e)
        raise ex
