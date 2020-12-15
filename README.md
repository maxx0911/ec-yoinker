# Downloading all emotes in the Emote Collector database
---
A step by step instruction on getting and downloading all emotes in the Emote Collector database.

## 0. install the requirements 
Two non-standard packages are required to run this project:
- yarl
- requests  

`yarl` (yet another url library) was my package of choice for working with URLs. `requests` is used to handle API requests and download emojis from Discord.  
You can install these two using pip like so: 
```sh
# Windows
pip install -U yarl requests

# Linux/Mac
python3 -m pip install -U yarl requests
```

## 1. grabbing all emote objects
This step is done via the Emote Collector API.  
You can get up to 250 emote objects at a time.

Emote objects contain the emoji ID, creator ID, NSFW status and other, not so relevant information.

To grab all emoji objects, first create a file called `config.py` in the same directory as `grabber.py`. This file should contain your API token in this format: 
```py
TOKEN = "Your token here"
```
You can receive an API token by using the command `ec/api token`, the bot will generate one for you.

After that, run `grabber.py` and, when prompted, input how many emotes there are overall (use `ec/list` for this, the number is at the bottom of the embed). This will take a while. 

After every request, there will be a 5 second delay before the next one. This is made so that no ratelimits will be exceeded. The API documentation does not mention ratelimits, but you can never be too sure.

This process will create a file named `emotes.json`, containing all emote data. It is possible that there are duplicates, but we will get rid of those in the next step.

## 2. formatting the emote objects
In this step, since emote objects don't have a download URL on their own, a download URL will be generated for all emote objects. This is done by checking whether an emote is animated (append .gif), or static (append .png).

The neat thing about Discord's cdn is that they store saved images as webp, png, and jpg, all at the same time, so we don't have to worry about getting jpg vs png right.

Simply run `formatter.py` to complete this step. This will generate a file named `emotes_updated.json`, which contains the same info as `emotes.json`, with addition of the URL parameter. When prompted, you can generate a list of URLs too, this could be used for more efficient downloading, if you know of a better method.

## 3. downloading the emotes
The last step is of course downloading all the emotes. After all, an emoji's ID is only half as useful as having the whole thing.

You can run `downloader.py` to get all of these emotes. They will be sorted into folders `nsfw` and `sfw`, depending on the emote object's NSFW status. 

> Note: not all emotes marked as SFW and really safe. Many users don't know that emotes can/should be marked as NSFW, and the mods generally only inspect newly added emotes.  

Depending on your network's download speed, this can take a while.  
When I did this originally on the 12/13/2020, we had about 15k emotes and 650MB of disk space, which took about an hour (even though my download speed is faster than that).