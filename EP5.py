import discord
from discord.ext import commands
import json
import random

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='[', intents=intents)

@bot.event
async def on_ready():
    print('>> bot is online <<')

@bot.command()
async def 圖片(ctx):
    pic = discord.File(jdata['pic'])
    await ctx.send(file = pic)

@bot.command()
async def 隨機圖片(ctx):
    random_pic = random.choice(jdata['pic'])
    pic = discord.File(random_pic)
    await ctx.send(file = pic)

@bot.command()
async def web(ctx):
    random_pic = random.choice(jdata['url_pic'])
    await ctx.send(random_pic)

bot.run(jdata['TOKEN'])