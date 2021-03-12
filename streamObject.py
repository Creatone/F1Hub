
class streamObj:
    def __init__(self, name, url, typeDef="none"):
        self.name = name
        self.url = url
        self.type = typeDef

    def getName(self):
        return self.name

    def getUrl(self):
        return self.url

    def getType(self):
        return self.type

    def getSelf(self):
        return self