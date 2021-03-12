import requests

def checkForUpdate():
    try:
        r = requests.get("https://raw.githubusercontent.com/kodosexe/F1Hub/main/version")
        existing = open('./version', 'r').read()
        #print(r.text)
        if r.text == existing:
        #    print("No update found")
            return False
        else:
        #    print("Update Available")
            return True
    except:
        return False