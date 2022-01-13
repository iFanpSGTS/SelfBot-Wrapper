import json
import requests, time, random
from .error import *

class Route:
    def __init__(self, token, useragent, xsp):
        self.token = token
        self.useragent = useragent
        self.xsp = xsp
        self.session = requests.Session()
        self.headers = {'authorization': self.token}
        if useragent:
            self.headers['user-agent'] = self.useragent
        if xsp:
            self.headers['x-super-properties'] = self.xsp
        self.session.headers.update(self.headers)
    
    def routesender(self, method, endpoint, data=None):
        respone_status = None
        if method == "DELETE":
            self.session.delete("https://discord.com/api" + endpoint, json=data)
        elif method == "GET":
            if endpoint == "https://latency.discord.media/rtc":
                self.session.get(endpoint, json=data)
            else:
                self.session.get("https://discord.com/api" + endpoint, json=data)
        elif method == "PATCH":
            self.session.patch("https://discord.com/api" + endpoint, json=data)
        elif method == "POST":
            self.session.post("https://discord.com/api" + endpoint, json=data)
        elif method == "PUT":
            self.session.put("https://discord.com/api" + endpoint, json=data)
        
        if respone_status.status_code == 401:
            raise InvalidToken
        elif respone_status.status_code == 403:
            raise Forbidden
        elif respone_status.status_code == 404:
            raise NotFound
        elif respone_status.status_code == 400:
            raise BadRequest
        else:
            return respone_status