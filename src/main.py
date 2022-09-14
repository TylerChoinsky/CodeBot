# This example requires the 'message_content' intent.

from ast import arguments
from helpers import *
import discord
import logging

# Init logging
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# Init Client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Event Handling
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # MOVE ALL THIS SHITTY CODE INTO A HELPER FUNCTION.
    if message.content.startswith('.run'):
        out = message_to_exec(message = message.content)
        await message.channel.send(out)

client.run('Iaccidentlypushedmytokentogithublol', log_handler=handler, log_level=logging.DEBUG)