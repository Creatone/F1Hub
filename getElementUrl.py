import requests
import json
import streamObject
import time
class getElement:
    def __init__(self, url):
        self.archiveURL = 'https://f1tv.formula1.com/2.0/R/ENG/WEB_DASH/ALL/PAGE/493/F1_TV_Pro_Monthly/2'
        self.baseURL = 'https://f1tv.formula1.com'
        self.targetURL = self.baseURL + url

    def getResultObj(self):
        r = requests.get(self.targetURL)
        return json.loads(r.text)

    def getCats(self):
        json = self.getResultObj()
        categories = []

        mx = json['resultObj']['total']-2
        for x in range(mx):
            t = x+2
            label = json['resultObj']['containers'][t]['metadata']['label']
            categories.append(label)

        return categories

    def getElements(self, cat):
        json = self.getResultObj()
        streamObjList = []
        category = cat + 2

        # Get from resultObj -> containers[2] -> retrieveItems -> resultObj -> total
        mx = json['resultObj']['containers'][category]['retrieveItems']['resultObj']['total']
        for x in range(mx):
            name = json['resultObj']['containers'][category]['retrieveItems']['resultObj']['containers'][x]['metadata']['title']
            url = json['resultObj']['containers'][category]['retrieveItems']['resultObj']['containers'][x]['actions'][0]['uri']
            element = streamObject.streamObj(name, url, "element")
            streamObjList.append(element)
        return streamObjList