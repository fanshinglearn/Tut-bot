# setting.json 設定檔
import discord
from discord.ext import commands
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='[', intents=intents)

@bot.event
async def on_ready():
    print('>> bot is online <<')

@bot.event
async def on_member_join(members):
    channel = bot.get_channel(int(jdata['Welcome_channel']))
    await channel.send(f'{members} join!')

@bot.event
async def on_member_remove(members):
    channel = bot.get_channel(int(jdata['Leave_channel']))
    await channel.send(f'{members} leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} (ms)')

bot.run(jdata['TOKEN'])