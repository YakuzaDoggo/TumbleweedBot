import sys
import os
import nextcord
from nextcord import Interaction
from nextcord import slash_command
from nextcord.ext import commands
from random import randint
import asyncio
import Tumbleweed

class user(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="start")
    async def start_sending(self, ctx):
            chID = ctx.channel.id

            for x in Tumbleweed.ChList:
                if x == chID:
                    await ctx.send("This channel " + "\(" + str(ctx.channel.id) + "\)" + " is already in the posting list!")
                    return

            Tumbleweed.ChList.append(ctx.channel.id)
            await ctx.send("Add this channel to the posting list!")
            await sleep(1)
            await ctx.send("Note that you can't remove a channel yet.\nNor will each channel have a unique timer (this might be annoying if you use this command in several channels)")

    @nextcord.slash_command(name = "start", description = "Add current Channel ID to the posting list.")
    async def start_sending(self, ctx):
            chID = ctx.channel.id

            for x in Tumbleweed.ChList:
                if x == chID:
                    await ctx.send("This channel " + "\(" + str(ctx.channel.id) + "\)" + " is already in the posting list!")
                    
                    return

            Tumbleweed.ChList.append(ctx.channel.id)
            await ctx.send("Add this channel to the posting list!")
            await sleep(1)
            await ctx.send("Note that you can't remove a channel yet.\nNor will each channel have a unique timer (this might be annoying if you use this command in several channels)")

def setup(bot):
  bot.add_cog(user(bot))
