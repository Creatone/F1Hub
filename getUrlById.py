import requests
import json
import streamObject

class getUrlByContentId:
    def __init__(self, id):
        self.contentID = id
        self.jsonObj = self.makeRequest(self.contentID)

    def makeRequest(self, id):
        if str(id) == "":
            return 0
        baseUrl = "https://f1tv.formula1.com/2.0/R/ENG/WEB_DASH/ALL/CONTENT/VIDEO/"+str(id)+"/F1_TV_Pro_Monthly/14?contentId="+str(id)+"&entitlement=F1_TV_Pro_Monthly"
        r = requests.get(baseUrl)
        if not r.status_code == 200:
            return -1
        j = json.loads(r.text)
        return j

    def grabType(self):
        videoType = self.jsonObj['resultObj']['containers'][0]['metadata']['videoType']
        title = self.jsonObj['resultObj']['containers'][0]['metadata']['titleBrief']
        subtype = self.jsonObj['resultObj']['containers'][0]['metadata']['contentSubtype']
        conc = videoType + " " + title + " " + subtype
        return conc

    def getContentID(self):
        return self.contentID

    def getObjName(self):
        return self.jsonObj['resultObj']['containers'][0]['metadata']['title']

    def getAdditionalStreams(self):
        streamList = []

        # First, return World Feed
        name = "World Feed"
        url = "CONTENT/PLAY?contentId=" + str(self.contentID)
        streamObj = streamObject.streamObj(name, url, "streamLink")
        streamList.append(streamObj)

        #Check if there are additional streams
        try:
            length = len(self.jsonObj['resultObj']['containers'][0]['metadata']['additionalStreams'])
        except:
            return streamList

        # If we are here, then yes.
        # First, filter out the non-onboard cams
        for x in range(length):
            if not self.jsonObj['resultObj']['containers'][0]['metadata']['additionalStreams'][x]['type'] == 'obc':
                if self.jsonObj['resultObj']['containers'][0]['metadata']['additionalStreams'][x]['title'] == 'TRACKER':
                    name = 'Driver Tracker'
                elif self.jsonObj['resultObj']['containers'][0]['metadata']['additionalStreams'][x]['title'] == 'PIT LANE':
                    name = 'Pit Lane Channel'
                elif self.jsonObj['resultObj']['containers'][0]['metadata']['additionalStreams'][x]['title'] == 'DATA':
                    name = 'Data Channel'
                else:
                    name = 'Unknown Channel'

                url = self.jsonObj['resultObj']['containers'][0]['metadata']['additionalStreams'][x]['playbackUrl']
                streamObj = streamObject.streamObj(name, url, "streamLink")
                streamList.append(streamObj)
            
        for x in range(length):
            if self.jsonObj['resultObj']['containers'][0]['metadata']['additionalStreams'][x]['type'] == 'obc':
                fname = self.jsonObj['resultObj']['containers'][0]['metadata']['additionalStreams'][x]['driverFirstName']
                lname = self.jsonObj['resultObj']['containers'][0]['metadata']['additionalStreams'][x]['driverLastName']
                name = fname + " " + lname
                url = self.jsonObj['resultObj']['containers'][0]['metadata']['additionalStreams'][x]['playbackUrl']
                streamObj = streamObject.streamObj(name, url, "streamLink")
                streamList.append(streamObj)
        return streamList


    def printStrList(self):
        strList = self.getAdditionalStreams()
        for x in range(len(strList)):
            print(strList[x].getName(), strList[x].getUrl())
