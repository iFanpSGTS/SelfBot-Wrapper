from .route import Route

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
        result = self.route.routesender("DELETE", f"/v8/channels/{channelId}")
        return result.json()
    
    def DelMsg(self, channelId, msgId):
        result = self.route.routesender("DELETE", f"/v8/channels/{channelId}/messages/{msgId}")
        return result.json()
    
    def DelRole(self, guildId, roleId):
        result = self.route.routesender("DELETE", f"/v8/guilds/{guildId}/roles/{roleId}")
        return result.json()
        
    def GroupRemoveFriend(self, groupId, friendId):
        result = self.route.routesender("DELETE", f"/v8/channels/{groupId}/recipients/{friendId}")
        return result.json()
    
    def KickMember(self, guildId, userId, reason):
        result = self.route.routesender("DELETE", f"/v8/guilds/{guildId}/members/{userId}?reason={reason}")
        return result.json()
    
    def RevokeBan(self, guildId, userId):
        result = self.route.routesender("DELETE", f"/v8/guilds/{guildId}/bans/{userId}")
        return result.json()
    
class PostWrapper:
    def __init__(self, token, useragent=None, xsp=None):
        self.token = token
        self.useragent = useragent
        self.xsp = xsp
        self.route = Route(self.token, self.useragent, self.xsp)
        
    def CreateChannel(self, channelName, guildId, parentId=None, nfsw=False):
        payload = {
        "type":0,
        "name": channelName,
        "permission_overwrites":[],
        "parent_id": parentId,
        "nsfw": nfsw
        }
        result = self.route.routesender("POST", f"/v8/guilds/{guildId}/channels", payload)
        return result.json()
    
    def CreateDM(self, recipientId):
        payload = {
            "recipients":[
                f"{recipientId}"
            ]
        }
        result = self.route.routesender("POST", "/v8/users/@me/channels", payload)
        return result.json()
    
    def CreateGroup(self, friendId):
        payload = {
            "recipients":[
                f"{friendId}"
            ]
        }
        result = self.route.routesender("POST", "/v8/users/@me/channels", payload)
        return result.json()
    
    def CreateGuild(self, guildName):
        payload = {
            "name": guildName,
            "icon":None,
            "channels":[],
            "system_channel_id":None,
        }
        result = self.route.routesender("POST", "/v8/guilds", payload)
        return result.json()
    
    def CreateRole(self, guildId, roleName, permission=None, color=None, displayed=True, mentionAble=False):
        payload = {
            "name": roleName,
            "permissions": permission,
            "color": color, # RGB value
            "hoist": displayed, #whether the role should be displayed separately in the sidebar
            "mentionable": mentionAble
        }
        result = self.route.routesender("POST", f"/v8/guilds/{guildId}/roles", payload)
        return result.json()
    
    def SendImg(self, filePath, channelId):
        payload = {
            'Content-Disposition': f'form-data; name="file"; filename="ifanps-sendimg-selfbot.png"',
            'Content-Type': 'image/png',
        }
        file = {
            'file': filePath
        }
        result = self.route.routesender("POST", f"/v8/channels/{channelId}/messages", payload, file)
        return result.json()
    
    def SendMsg2Channel(self, channelId, msg):
        payload = {
            'content': msg
        }
        result = self.route.routesender("POST", f"/v8/channels/{channelId}/messages", payload)
        return result.json()
    
class PatchWrapper:
    def __init__(self, token, useragent=None, xsp=None):
        self.token = token
        self.useragent = useragent
        self.xsp = xsp
        self.route = Route(self.token, self.useragent, self.xsp)
        
    def MuteChannel(self, guildId, channelId):
        payload = {
            "channel_overrides":{
            channelId:{
            "muted":True,
            }}}
        result = self.route.routesender("PATCH", f"/v8/users/@me/guilds/{guildId}/settings", payload)
        return result.json()
    
    def UnmuteChannel(self, guildId, channelId):
        payload = {
            "channel_overrides":{
            channelId:{
            "muted":False,
            }}}
        result = self.route.routesender("PATCH", f"/v8/users/@me/guilds/{guildId}/settings", payload)
        return result.json()
