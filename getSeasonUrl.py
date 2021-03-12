import requests
import json
import streamObject

class getSeason:
    def __init__(self):
        self.archiveURL = 'https://f1tv.formula1.com/2.0/R/ENG/WEB_DASH/ALL/PAGE/493/F1_TV_Pro_Monthly/2'
        self.baseURL = 'https://f1tv.formula1.com/'

    def getResultObj(self):
        r = requests.get(self.archiveURL)
        return json.loads(r.text)

    # Return obj containing endpoint url and Year of season
    def getAllSeasons(self):
        json = self.getResultObj()
        streamObjList = []
        
        # Go through resultObj -> containers[2] -> retrieveItems -> resultObj -> containers
        for x in range(json['resultObj']['containers'][2]['retrieveItems']['resultObj']['total']):
            name = json['resultObj']['containers'][2]['retrieveItems']['resultObj']['containers'][x]['metadata']['longDescription']
            url = json['resultObj']['containers'][2]['retrieveItems']['resultObj']['containers'][x]['actions'][0]['uri']
            #print(name, url)
            streamObj = streamObject.streamObj(name, url, 'f1tvseason')
            streamObjList.append(streamObj)


        # Go through resultObj -> containers[6-10]
        for i in range(6,10):
            # Go through resultObj -> containers[i] -> retrieveItems -> resultObj -> containers
            for x in range(json['resultObj']['containers'][i]['retrieveItems']['resultObj']['total']):
                name = json['resultObj']['containers'][i]['retrieveItems']['resultObj']['containers'][x]['metadata']['emfAttributes']['Global_Meeting_Name']
                url = json['resultObj']['containers'][i]['retrieveItems']['resultObj']['containers'][x]['actions'][0]['uri']
                if not name == "":
                    #print(name, url)
                    stream = streamObject.streamObj(name, url, 'f1tvseason')
                    streamObjList.append(stream)
                    #print(streamObjList[len(streamObjList)-1].getName())
        #print(streamObjList[3].getName())
        return streamObjList
    