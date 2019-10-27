# bot.py
import os
import re
import random
import requests

import discord
from dotenv import load_dotenv

from modules import xingamento, connect_voice, reddit


load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

# @client.event
# async def on_ready():
#     reddit.reddit_class('modernwarfare')

@client.event
async def on_message(message):
    if message.author == client.user:
            return
    if message.content.startswith('!'):

        if message.content.startswith('!xingamento'):
            await xingamento.xingamento(message)

        if message.content.startswith('!entrar'):
            await connect_voice.connect_user_voice(message)
        
        if message.content.startswith('!sair'):
            await connect_voice.disconnect_user_voice(message)

        if message.content.startswith('!sub'):
            client.loop.create_task(reddit.subscribe(message, re.sub('!sub ', '', message.content)))

client.run(token)