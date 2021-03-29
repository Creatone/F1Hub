# F1Hub
## A Python Client to View F1TV Content _the right way_



F1Hub is a terminal application running directly on your computer -- no connection to the website needed*
_*In theory. As of now, the F1TV website is needed for some content_

![F1Hub Main Menu](https://github.com/kodosexe/f1hubmisc/blob/main/f1Hub0-10.png?raw=true)


## Features
##### _What this is_

- No lenthy website load times
- Even if the website is down, usually the API stays available, which means F1Hub will be working as well.
- Designed to work with the 2021 updated F1TV API, delivering you 1080p50 streams by default.
- Multi-Stream functionality: Unlike on the website, this tool opens as many streams as you like, enabling you to create your own Race Control at home.
- Simply enter a Content ID (long number in the URL of a play page) in the content ID menu and immediately play! No long menu browsing required.

## Anti-Features
##### _What this is not_
F1Hub is NOT a piracy tool. To use it, you will need to log in with your valid F1TV Credentials. To use livestream functionality, you will need to have an active F1TV Pro account.
This program is not related to F1, F1TV, FIA or any other organization. This is a fan-made application designed to get the most out of the service F1TV provides.

## Installation
##### _Cool, how do I get it?_
#### The simple way (Linux and MacOS, maybe Windows)
If you are on Linux (Tested on Ubuntu based systems) or MacOS, you can download the respective prepackaged file in the [release tab](https://github.com/kodosexe/F1Hub/releases). If you are on Windows, you will need to download the Linux package and use the [Windows Subsystem for Linux](https://docs.microsoft.com/learn/modules/get-started-with-windows-subsystem-for-linux/)
In a terminal, navigate to the folder containing the downloaded file (most likely 'downloads') and enter
```
sudo chmod +x f1Hub-$version-$os
./f1Hub-$version-$os
```

If the above steps don't work, proceed with the following steps:
#### Dependencies
##### Special steps for Windows
One of F1Hub's dependencies doesn't work with Windows. To use it, you will have to use the Windows Subsystem For Linux
You can find a guide on how to install and use it [here](https://docs.microsoft.com/learn/modules/get-started-with-windows-subsystem-for-linux/)
##### For all operating systems
First, let's install the dependencies.
Make sure you have pip installed:
```sh
pip --version
```
If the command gives you an output, you're good to go. If it says that the command 'pip' was not found, follow the [this guide](https://pip.pypa.io/en/stable/installing/) to install pip on your machine:
Now, use pip to install the needed dependencies
```sh
python3 -m pip install simple-term-menu pyperclip requests json
```
Some of these may already be preinstalled, depending on your machine and os.
Next, install the video player MPV, according to [this guide](https://mpv.io/installation/). To be sure, reboot your computer and type
```sh
mpv --version
```
into your Terminal to make sure it works and is in the PATH.
Done! Now let's get the main program:
#### Main Program
##### _Getting F1Hub_
Download F1Hub, either by cloning the repository, or by downloading it directly [from the releases tab](https://github.com/kodosexe/F1Hub/releases). To clone it:
```sh
git clone https://github.com/kodosexe/f1hub
```
Now, you can simply run it by executing 
```sh
cd f1Hub
python3 main.py
```
and you will be greeted by the Menu

## Usage
##### _How does it work?_
First, you should login. For that, use the arrow keys to navigate to F1TV Login and choose Login by Password. It is stored in plaintext on your computer for now, though, so be careful!
If you don't want to enter your password:
You will need to open [F1TV](f1tv.formula1.com) in your browser, right-click anywhere on the page, and select _"Inspect"_ from the menu.
In the bar that opens, select the _"Network"_ tab. Check the box saying _"Preserve Log"_. In Firefox, this option will appear when you click on the gears and is named _"Persist Logs"_
Now, log in, as with any other website. The tab should fill with a list of network requests. Once you are logged in, type _"ENTITLEMENT"_ into the search bar of the inspector tab. There should be one entry of that name. Right click on the entry and select _"Copy -> Copy Response"_. The information was copied to your clipboard
In the folder containing F1Hub, open or create the file named _"entitlement.json"_ and paste your clipboard.

After restarting F1Hub, you can use it fully. You may need to repeat that step occasionally. Usually, when F1Hub crashes and gives you an error, it will be due to entitlement or login issues.

##### How to work with the ContentID
To play a stream using content ID, first navigate to the video [in your browser](f1tv.formula1.com). You will see a long sequence of numbers in the URL, something like _"1000000716"_. That is the content ID. Copy that number and paste it into F1Hub in the _"Play by Content ID"_ menu. Proceed like normal.
## Known Bugs
##### _Whoopsie_
 - 2020 Preaseason Testing doesn't include full sessions. This is because this is the only event that has a different API response structure. I plan on fixing this soon.
 - The menu sometimes spazzes out in seasons before 2018. This is because of long titles resulting by a mishandling of the API - this is low priority because these sessions have only one stream. The main purpose of this program is to provide a multi-stream service. However, I do plan on fixing it at some point down the line.
 - Some menus only show partial content, none at all, or provide no stream. The API pre-2017 is wildly different. I didn't realize until too late and it will be patched at some point. 2020-2018 Work flawlessly, though
 - 2021 Sessions and Info not available. Current season is not implemented yet, as there is no info on the buildup. It will come at some point before the season.
 - There is little to no error handling... if something goes wrong, it will crash. Please keep in mind, this program, including all API analysis was built in little over 24Hrs. It will have bugs and issues.

## Planned Features
##### _What the future has in stock_
- All the bug fixes!
- Better, more flexible menu structure, and a graphical UI down the line.
- Live feature before the season's start _-NOW AVAILABLE_
- 2021 Integration before the season's start _-Available via ContentID feature_
- Any Event based on ID being able to be played, ideally before the season's start. _-NOW AVAILABLE_

I am now working on the first full release of F1Hub - It will have better menu structure, better aesthetics, proper error handling, safer password login and native and easy windows support.
_Here's a work in progress sneak peek picture of F1Hub v1, featuring a GUI:_
![Sneak Peek picture of F1Hub with a Graphical User Interface](https://github.com/kodosexe/f1hubmisc/blob/main/f1HubGuiSneakPeek.png?raw=true)

## Disclaimer
##### _Just to cover my back_
This program is provided as is, with no warranty whatsoever. I do not take responsibility for any damages or issues that may result from direct or indirect use of this program.
