import requests
import json
import emoji

class createinstance:
    def __init__(self,token,apiversion=9):
        self.token = token
        self.headers = {
            'Authorization': self.token
        }
        if (apiversion == None):
            self.apiversion = 9
        else:
            self.apiversion = apiversion

    def sendmessage(self,content,channelid):
        data = {
            'content': content
        }
        r = requests.post(f"https://discord.com/api/{"v"+str(self.apiversion)}/channels/{channelid}/messages",headers=self.headers,data=data)
        return r.status_code
    def sendreply(self,content,channelid,messageid):
        data = {
            'content': content,
            'message_reference' : {
                "channel_id": channelid,
                "message_id": messageid
            }
        }
        r = requests.post(f"https://discord.com/api/{"v"+str(self.apiversion)}/channels/{channelid}/messages",headers=self.headers,json=data)
    def sendreaction(self,reactionemoji,channelid,messageid):
        r = requests.put(f"https://discord.com/api/{"v"+str(self.apiversion)}/channels/{channelid}/messages/{messageid}/reactions/{emoji.emojize(reactionemoji)}/@me",headers=self.headers)
        return r.status_code
    def createDM(self,userid):
        data = {
            "recipient_id": userid
        }
        r = requests.put(f"https://discord.com/api/{"v"+str(self.apiversion)}/users/@me/channels",headers=self.headers)
        return r.json['id']
    def readchannelmessages(self,channelid,limit=50):
        r = requests.get(f"https://discord.com/api/{"v"+str(self.apiversion)}/channels/{channelid}/messages?limit={str(limit)}",headers=self.headers)
        return json.loads(r.text)
    def getlatestmessage(self,channelid):
        r = requests.get(f"https://discord.com/api/{"v"+str(self.apiversion)}/channels/{channelid}/messages?limit=1",headers=self.headers)
        return json.loads(r.text)[0]