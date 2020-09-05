import discord
from discord.ext import commands
import os

client = commands.Bot(commands_prefix = '-')
@client.event
async def on_ready():
    # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
    await client.change_presence(status=discord.Status.online)
    await client.change_presence(activity=discord.Game(name="테스트중"))
    print("봇 이름:",client.user.name,"봇 아이디:",client.user.id,"봇 버전:",discord.__version__)

client.run(os.environ['token'])
