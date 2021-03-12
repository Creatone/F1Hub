import requests
import json
import streamObject
import time
class getStream:
    def __init__(self, url):
        self.archiveURL = 'https://f1tv.formula1.com/2.0/R/ENG/WEB_DASH/ALL/PAGE/493/F1_TV_Pro_Monthly/2'
        self.baseURL = 'https://f1tv.formula1.com'
        self.targetURL = self.baseURL + url

    def getResultObj(self):
        r = requests.get(self.targetURL)
        return json.loads(r.text)

    def getStreams(self):
        json = self.getResultObj()
        streamObjList = []
        
        name = "World Feed"
        link = 'CONTENT/PLAY?contentId='
        contId = str(json['resultObj']['containers'][0]['metadata']['contentId'])
        url = link + contId
        element = streamObject.streamObj(name, url, "feed")
        streamObjList.append(element)
        # Get from resultObj -> containers[0] -> metadata -> additionalStreams
        # If it's a race & has onboards:
        if json['resultObj']['containers'][0]['metadata']['emfAttributes']['OBC']:
            mx = len(json['resultObj']['containers'][0]['metadata']['additionalStreams'])
            for x in range(mx):
                if json['resultObj']['containers'][0]['metadata']['additionalStreams'][x]['type'] == 'additional':
                    name = json['resultObj']['containers'][0]['metadata']['additionalStreams'][x]['title']
                    url = json['resultObj']['containers'][0]['metadata']['additionalStreams'][x]['playbackUrl']
                    element = streamObject.streamObj(name, url, "element")
                    streamObjList.append(element)
                else:
                    fn = json['resultObj']['containers'][0]['metadata']['additionalStreams'][x]['driverFirstName']
                    ln = json['resultObj']['containers'][0]['metadata']['additionalStreams'][x]['driverLastName']
                    name = fn+ ' ' + ln
                    #print(name)
                    url = json['resultObj']['containers'][0]['metadata']['additionalStreams'][x]['playbackUrl']
                    element = streamObject.streamObj(name, url, "element")
                    streamObjList.append(element)
        else:
            pass
        return streamObjList