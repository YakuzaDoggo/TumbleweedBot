# TumbleweedBot
Stupid little bot I made after an idea was sent in a server... **3 YEARS AGO**.

# Ok, so what does it do?
It sends an image of a tumbleweed at random, to a defined channel that the user sets. That's it.

# Installation

**_Required_**
- [At least Python 3.8](https://www.python.org/downloads/)
- [Nextcord](https://github.com/nextcord/nextcord)

Edit the bot to your heart's content. Important things to keep note are:
- ``anchortime`` - The base time that will be used to wait for image sending.
- ``variance`` - A variance integer that is used along side anchortime to randomize the image sending interval.
- ./images/images - This is where images are kept at. I don't feel exactly comfortable making an entire repo licensed under GPL and include the images, so you'll need to find your own.

**It is imporant to add a bot's token to the program, or it won't work. You can add it at the bottom of Tumbleweed.py.**

Once done with that. Use your terminal, cd into the main folder, and run ``python3 Tumbleweed.py``.

# Limitation
- The bot relies on an overall timer for sending images. Meaning all channels are given an image at the exact time (albeit random images). This may be an annoyance where you have it added to multiple channels at once.
