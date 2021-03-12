import requests
from dataclasses import dataclass
import json

@dataclass
class f1tv:
    baseApi: str
    archive: str

f1tv.archive = "https://f1tv.formula1.com/2.0/R/ENG/WEB_DASH/ALL/PAGE/493/F1_TV_Pro_Monthly/2"
f1tv.baseApi = "https://f1tv.formula1.com"

r = requests.get(f1tv.archive)

jsonized = json.loads(r.text)
objList = jsonized['resultObj']['containers'][2]['retrieveItems']['resultObj']['containers'][0]['metadata']['longDescription']
objLink = jsonized['resultObj']['containers'][2]['retrieveItems']['resultObj']['containers'][0]['actions'][0]['uri']