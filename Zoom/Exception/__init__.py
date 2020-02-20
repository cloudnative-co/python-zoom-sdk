import urllib
import json

class APIException(urllib.error.HTTPError):
    _code = None

    def __init__(self, e: urllib.error.HTTPError):
        super()
        self.state = e.code
        self.hdrs = e.hdrs
        self.fp = e.fp
        self.filename = e.filename
        body = e.read().decode("utf-8")
        body = json.loads(body)
        self.msg = body["message"]
        self.code = body["code"]

    def __str__(self):
        return json.dumps({
            "message": self.msg,
            "code": self.code,
            "status": self.state,
            "reason": self.reason,
            "url": self.filename
        })
