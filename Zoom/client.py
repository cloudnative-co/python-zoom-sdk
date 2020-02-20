import base64
import hmac
import hashlib
import json
import urllib.request
import urllib.parse
from .Exception import APIException


class Client(object):
    headers: dict = dict()
    host: str = "api.zoom.us"
    version: str = "v2"
    schema = "https"
    token: str = None


    def __init__(
        self,
        api_key: str = None, api_secret: str = None,
        expire: int = 1496091964000, client = None
    ):
        if client is not None:
            self.host = client.host
            self.version = client.version
            self.headers = client.headers
            self.token = self.token
            self.schema = client.schema
        else:
            header = json.dumps({'typ': 'JWT', 'alg': 'HS256'}).encode('utf-8')
            henc = base64.urlsafe_b64encode(header).decode().strip('=')
            payload = json.dumps({"iss": api_key, "exp": expire}).encode('utf-8')
            penc = base64.urlsafe_b64encode(payload).decode().strip('=')
            hdata = henc + '.' + penc
            d = hmac.new(api_secret.encode('utf-8'), hdata.encode('utf-8'), 'sha256')
            dig = d.digest()
            denc = base64.urlsafe_b64encode(dig).decode().strip('=')
            token = hdata + '.' + denc
            self.token = token
            self.headers = {
                'authorization': "Bearer {}".format(token),
                'content-type': "application/json"
            }
            self.host = "api.zoom.us"
            self.version = "v2"

    def request(
        self,
        method: str, path: str,
        query: dict = None, payload: dict = None,
        to_dict: bool = True
    ):
        url = "{}://{}/{}{}".format(self.schema, self.host, self.version, path)
        if not ((query is None) or (len(query) == 0)):
            url = "{}?{}".format(url, urllib.parse.urlencode(query))
        args = {
            "url": url,
            "headers": self.headers
        }
        if payload is not None:
            payload = urllib.parse.urlencode(payload).encode("utf-8")
        else:
            payload = b""

#        req = urllib.request.Request(url, headers=self.headers)
        req = urllib.request.Request(**args)
        try:
            with urllib.request.urlopen(req) as res:
                body = res.read().decode("utf-8")
                if to_dict:
                    return json.loads(body)
                else:
                    return body
        except urllib.error.HTTPError as e:
            ex = APIException (e)
            raise ex
