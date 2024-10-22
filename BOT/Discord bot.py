# Imports from the .env and the requirements.txt

from subprocess import call
from dotenv import load_dotenv
import os
import discord
import json
import climage
from PIL import Image
from discord.ext.commands import bot
import random

image = Image.open("images/mario.gif")
load_dotenv()

# Client of discord

client = discord.Client(intents=discord.Intents.default())


# bot is ready and will paste we have logged in as user in the terminal


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


# the command to out print Heya! when put in the command $hello in the chat


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    message.content.startswith("!hello")
    await message.channel.send("Heya!")

    @client.command
    async def png(ctx):
        if message.author == client.user:
            return

    if message.content.startswith == "mario":
        await message.channel.send(file=discord.File("images/mario.gif"))

        print("Letsa Go!!")


client.run(os.getenv("TOKEN"))
