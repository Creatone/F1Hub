# F1Hub
## A Python Client to View F1TV Content _the right way_



F1Hub is a terminal application running directly on your computer -- no connection to the website needed*
_*In theory. As of now, the F1TV website is needed for some content_

![alt text](https://github.com/kodosexe/f1hubmisc/blob/main/screenshot.png?raw=true)


## Features
##### _What this is_

- No lenthy website load times
- Even if the website is down, usually the API stays available, which means F1Hub will be working as well.
- Designed to work with the 2021 updated F1TV API, delivering you 1080p50 streams by default
- Multi-Stream functionality: Unlike on the website, this tool opens as many streams as you like, enabling you to create your own Race Control at home
- Simply enter a Content ID (long number in the URL of a play page) in the content ID menu and immediately play! No long menu browsing required.

## Anti-Features
##### _What this is not_
F1Hub is NOT a piracy tool. To use it, you will need to log in with your valid F1TV Credentials. To use livestream functionality, you will need to have an F1TV Pro account.
As of now (1 Week ahead of 2021 Preseason testing), there is NO livestream functionality, as there is no way to test it properly.
I will be working on it during preseason and aim at having it implemented by start of the season.

## Installation
###### _Cool, how do I get it?_
#### Dependencies
First, let's install the dependencies.
Make sure you have pip installed:
```sh
pip -v
```
If the command gives you an output, you're good to go. If it says that the command 'pip' was not found, follow the [this guide](https://pip.pypa.io/en/stable/installing/) to install pip on your machine:
Now, use pip to install Simple Term Menu
```sh
python3 -m pip install simple-term-menu
```
Next, install the video player MPV, according to [this guide](https://mpv.io/installation/). To be sure, reboot your computer and type
```sh
mpv --version
```
into your Terminal to make sure it works and is in the PATH
Done! Now let's get the main program:
#### Main Program
Download F1Hub, either by cloning the repository, or by downloading it directly. To clone it:
```sh
git clone https://github.com/kodosexe/f1hub
```
Now, you can simply run it by executing 
```sh
python3 main.py
```
and you will be greeted by the Menu

## Usage

Login by password is now available! It is stored in plaintext on your computer for now, though, so be careful!
Otherwise:
You will need to open [F1TV](f1tv.formula1.com) in your browser, right-click anywhere on the page, and select _"Inspect"_ from the menu.
In the bar that opens, select the _"Network"_ tab. Check the box saying _"Preserve Log"_. In Firefox, this option will appear when you click on the gears and is named _"Persist Logs"_
Now, log in, as with any other website. The tab should fill with a list of network requests. Once you are logged in, type _"ENTITLEMENT"_ into the search bar of the inspector tab. There should be one entry of that name. Right click on the entry and select _"Copy -> Copy Response"_. The information was copied to your clipboard
In the folder containing F1Hub, open or create the file named _"entitlement.json"_ and paste your clipboard.

After restarting F1Hub, you can use it fully. You may need to repeat that step occasionally. Usually, when F1Hub crashes and gives you an error, it will be due to entitlement issues.

##### How to work with the ContentID
To play a stream using content ID, first navigate to the video [in your browser](f1tv.formula1.com). You will see a long sequence of numbers in the URL, something like _"1000000716"_. That is the content ID. Copy that number and paste it into F1Hub in the _"Play by Content ID"_ menu. Proceed like normal.
This _may_ work for live sessions, if they are designed the same way. We will know when Preseason testing comes around.
## Known Bugs
 - 2020 Preaseason Testing doesn't include full sessions. This is because this is the only event that has a different API response structure. I plan on fixing this soon.
 - The menu sometimes spazzes out in seasons before 2018. This is because of long titles resulting by a mishandling of the API - this is low priority because these sessions have only one stream. The main purpose of this program is to provide a multi-stream service. However, I do plan on fixing it at some point down the line.
 - Some menus only show partial content, none at all, or provide no stream. The API pre-2017 is wildly different. I didn't realize until too late and it will be patched at some point. 2020-2018 Work flawlessly, though
 - 2021 Sessions and Info not available. Current season is not implemented yet, as there is no info on the buildup. It will come at some point before the season.
 - There is NO error handling... if something goes wrong, it will crash. Please keep in mind, this program, including all API analysis was built in little over 24Hrs. It will have bugs and issues.

## Planned Features
- All the bug fixes!
- Better, more flexible menu structure, and a graphical UI down the line.
- Live feature before the season's start
- 2021 Integration before the season's start
- Any Event based on ID being able to be played, ideally before the season's start. _NOW AVAILABLE_

## Disclaimer
This program is provided as is, with no warranty whatsoever. I do not take responsibility for any damages or issues that may result from direct or indirect use of this program. Just to cover my back.
