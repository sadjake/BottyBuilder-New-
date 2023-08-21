from SECRET import token
import nextcord, time
#from nextcord import Interaction
from nextcord.ext import commands

#import logging
#import os
#from typing import Optional

#logging.basicConfig(level=logging.INFO)
#activity = nextcord.Activity(type=nextcord.ActivityType.listening, name="/hello")

#intents = nextcord.Intents.default()
#intents.members = True

bot = commands.Bot();

@bot.event
async def on_ready():
    print("The bot, {bot.user}, is ready!")

@bot.slash_command(description="My first slash command")
async def hello(interaction: nextcord.Interaction):
    await interaction.send("Hello!")