# TumbleweedBot
Stupid little bot I made after an idea was sent in a server... **3 YEARS AGO**.

# Ok, so what does it do?
It sends an image of a tumbleweed at random, to a defined channel that the user sets. That's it.

# Installation
*Note that if you wish to use the bot, you can always invite it using [this link](https://discord.com/oauth2/authorize?client_id=1124911330328055828&scope=bot&permissions=100352).*

**_Required_**
- [At least Python 3.8](https://www.python.org/downloads/)
- [Nextcord](https://github.com/nextcord/nextcord)

Edit the bot to your heart's content. Important things to keep note are:
- ``anchortime`` - The base time that will be used to wait for image sending.
- ``variance`` - A variance integer that is used along side anchortime to randomize the image sending interval.
- ./images/images - This is where images are kept at. I don't feel exactly comfortable making an entire repo licensed under GPL and include the images, so you'll need to find your own.

**It is imporant to add a bot's token to the program, or it won't work. You can add it at the bottom of Tumbleweed.py.**

Once done with that. Use your terminal, cd into the main folder, and run ``python3 Tumbleweed.py``.

# Limitations
- Currently, you can *add* a channel, but you can not *remove* one. If you don't want the bot to send to a channel, just remove its perms to send messages there (or kick it).
- The bot relies on an overall timer for sending images. Meaning all channels are given an image at the exact time (albeit random images). This may be an annoyance where you have it added to multiple channels at once.
