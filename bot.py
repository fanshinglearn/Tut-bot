import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='[', intents=intents)

@bot.event
async def on_ready():
    print('>> bot is online <<')

@bot.event
async def on_member_join(members):
    channel = bot.get_channel(1188555511658975263)
    await channel.send(f'{members} join!')

@bot.event
async def on_member_remove(members):
    channel = bot.get_channel(1188555562565251253)
    await channel.send(f'{members} leave!')

bot.run('MTE4ODExNDg3NDExMTM2MTEwNQ.G7vmOm.8r5J24kxrOonAFJhN-xjCtdfBkIgzIfOxC5YLI')