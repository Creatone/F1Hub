import requests
import json
import streamObject
import time


class getTokenizedUrl:
    def __init__(self, url, authObj):
        self.basePlayUrl = 'https://f1tv.formula1.com/1.0/R/ENG/WEB_HLS/ALL/'
        self.url = self.basePlayUrl + url
        self.authObj = authObj

    def getUrl(self):
        token = self.authObj.getEntitlementToken()
        params = {'entitlementtoken': token}
        r = requests.get(self.url, headers=params)
        jso = json.loads(r.text)
        url = jso['resultObj']['url']
        return url