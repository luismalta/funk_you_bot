# bot.py
import os
import random
import requests

import discord
from dotenv import load_dotenv


load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
            return

    response = requests.get('http://xinga-me.appspot.com/api').json()['xingamento']

    if message.content == '!xingamento':
        await message.channel.send(response)

client.run(token)