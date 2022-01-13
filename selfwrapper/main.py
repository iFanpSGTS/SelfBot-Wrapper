from .route import Route
import random, base64, requests

class GetWrapper:
    def __init__(self, token, useragent=None, xsp=None):
        self.token = token
        self.useragent = useragent
        self.xsp = xsp
        self.route = Route(self.token, self.useragent, self.xsp)
        
    def GetCliInfo(self):
        result = self.route.routesender("GET", "/v8/users/@me").json()
        self.username = result['username']
        self.id = result['id']
        self.avatar = result['avatar']
        self.discriminator = result["discriminator"]
        self.public_flags = result["public_flags"]
        self.flags = result["flags"]
        self.email = result["email"]
        self.verified = result["verified"]
        self.locale = result["locale"]
        self.nsfw_allowed = result["nsfw_allowed"]
        self.mfa_enabled = result["mfa_enabled"]
        self.phone = result["phone"]
        return result
    
    def GetFriendConnection(self):
        result = self.route.routesender("GET", "/v8/users/@me/relationships")
        return result.json()
    
    def GetChannelMsg(self, channelId):
        result = self.route.routesender("GET", f"/v8/channels/{channelId}/messages")
        return result.json()
    
    def GetConnectionApp(self):
        result = self.route.routesender("GET", "/v8/users/@me/connections")
        return result.json()
    
    def CheckIP(self):
        result = self.route.routesender("GET", "https://latency.discord.media/rtc")
        return result.json()
    
class DeleteWrapper:
    def __init__(self, token, useragent=None, xsp=None):
        self.token = token
        self.useragent = useragent
        self.xsp = xsp
        self.route = Route(self.token, self.useragent, self.xsp)
        
    def DelCategory(self, categoryId):
        result = self.route.routesender("DELETE", f"/v8/channels/{categoryId}")
        return result.json()
    
    def DelChannel(self, channelId):
        result = self.route.routesender("DELETE", f"v8/channels/{channelId}")
        return result.json()