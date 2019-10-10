# bot.py
import os
import random

import discord
from dotenv import load_dotenv


load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
            return

    xingamento_list = [
        'Seu merda',
        'Bundão',
        'Pau no cú'
    ]

    if message.content == '!xingamento':
        response = random.choice(xingamento_list)
        await message.channel.send(response)

client.run(token)