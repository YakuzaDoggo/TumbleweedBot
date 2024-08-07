# Before using this code for any reason (running, editing) please read the license included in the LICENSE folder

import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from nextcord.ext.commands import bot
from nextcord.ext.commands import CommandNotFound
import os
import sys
import functions
sys.path.insert(0, './Images/')
import images
import random
import asyncio
import atexit

# anchortime is the "base" time used. variance adds/subtracts to that to randomize the interval between images
anchortime = 7200
variance = 3600

# lets bot read what is in messages
intents = nextcord.Intents.default()
intents.message_content = True


bot = commands.AutoShardedBot(shard_count = 3, command_prefix='.')

images = images.images

functions.UpdateArray()


# array used to store channels that are "subscribed" to getting messages
ChList = [ 
    ]


@bot.event 
async def on_ready():
    print("Logged in")

    print(bot.user)

    # adds saved channels to ChList
    with open("./ChList.txt", 'r') as file:
        for line in file:
            ChList.append(line.strip())
    
    # debugging text
    print("channels in array")
    for x in ChList:
        print(x)
    # start of bot sending random images
    while True:
        await SendTumbleweed(ChList)

# begin of cogs stuff (used for slash commands)
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
        raise error

@bot.command()
async def load(ctx, extension):
  bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
  bot.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')
# end of cogs (thank god)

# takes in ChList, calculates the time interval until posting, and posts the image to the channels
async def SendTumbleweed(list):
    
    # this is just checks if we add or subtract to the anchortime
    sign = random.randint(0, 1)

    if sign == 1:
        WaitTime = anchortime + random.randint(0, variance)
    else:
        WaitTime = anchortime + (-1 * random.randint(0, variance))
    
    await asyncio.sleep(WaitTime)

    if len(ChList) == 0:
        print("there are no channels :(")
        return
    else:
        for item in ChList:
            channelid = int(item)

            print("Sending image to " + str(channelid))

            channel = bot.get_channel(channelid)

            await channel.send(file=nextcord.File(images[random.randint(0, len(images)-1)]))

# writes all channel ID's in ChList to text file to save list
def exit_handler():
    with open('./ChList.txt', 'w') as file:
            for x in ChList:
                file.write(str(x) + '\n')

atexit.register(exit_handler)

# BE SURE TO ADD YOUR TOKEN OR ELSE BOT WILL NOT WORK
token = "[TOKEN_GOES_HERE]"
bot.run(token)
