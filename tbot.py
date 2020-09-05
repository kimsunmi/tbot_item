import discord
import os
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="itemShop",type=1))
    print("this is item shop. welcome!")

@client.event
async def on_message(message):
    id = message.author.id
    if message.content.startswith('!itemlist'):
        await client.send_message('Ha ha, What do you want?')
    await message.channel.send()

client.run(os.environ['token'])
