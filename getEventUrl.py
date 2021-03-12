import requests
import json
import streamObject
import time

class getEvent:
    def __init__(self, url):
        self.targetUrl = 'https://f1tv.formula1.com' + url

    def getResultObj(self):
        r = requests.get(self.targetUrl)
        if r.status_code == 200:
            return json.loads(r.text)
        else:
            print("Event get failed")
            exit
            return '{}'

    def getAllEvents(self):
        json = self.getResultObj()
        streamObjList = []

        # Go thtough resultObj -> containers(max) -> retrieveItems -> resultObk -> total
        # Get the max of the first containers
        mx = json['resultObj']['total']-1

        for x in range(json['resultObj']['containers'][mx]['retrieveItems']['resultObj']['total']):
            name = json['resultObj']['containers'][mx]['retrieveItems']['resultObj']['containers'][x]['metadata']['longDescription']
            url = json['resultObj']['containers'][mx]['retrieveItems']['resultObj']['containers'][x]['actions'][0]['uri']
            stream = streamObject.streamObj(name, url, 'f1tvevent')
            streamObjList.append(stream)

        return streamObjList