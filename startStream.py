import platform
import subprocess
import time

class startStream:
    def __init__(self):
        self.osType = platform.system()
        print(self.osType)

    def start(self, url):
        if self.osType == "Linux":
            self.startLinux(url)
        elif self.osType == "Windows":
            self.startWindows(url)
        elif self.osType == "Darwin":
            self.startMacOS(url)
        else:
            print("Could not identify System... Please open a github issue")
            time.sleep(10)

    def startLinux(self, url):
        try:
            subprocess.call(["gnome-terminal", "-x", "mpv", "--border=no", url])
        except:
            print("Could not start Linux stream")
            time.sleep(10)
        
    def startWindows(self, url):
        try:
            subprocess.call('start /wait mpv --border=no ' + url, shell=True)
        except:
            print("Could not start Windows stream")
            time.sleep(10)

    def startMacOS(self, url):
        try:
            subprocess.call(['open', '-W', '-a', 'Terminal.app', 'mpv', '--border=no', url])
        except:
            print("Could not start Windows stream")
            time.sleep(10)