# 成員 加入/離開 事件
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
    channel = bot.get_channel(1217763083288580136)
    await channel.send(f'{members} join!')

@bot.event
async def on_member_remove(members):
    channel = bot.get_channel(1217763163378810890)
    await channel.send(f'{members} leave!')

bot.run('MTE4ODExNDg3NDExMTM2MTEwNQ.GTJgOR.uP8-f688QG_z5XSVwHxttI3zPokl3kacLaweLg')