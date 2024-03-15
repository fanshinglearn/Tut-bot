import discord
from discord.ext import commands
import json
import random

# 打開 setting.json 設定檔案
with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

# intents default 或 all 或 none
# 要打指令需要 ? 權限
intents = discord.Intents.all()
# intents = discord.Intents.default()

# 打該 members 的權限
# intents.members = True

# command_prefix 命令前綴
bot = commands.Bot(command_prefix='[', intents=intents)

# 啟動
@bot.event
async def on_ready():
    print('>> bot is online <<')

# <---------- menbers ---------->
# 成員加入
@bot.event
async def on_member_join(members):
    channel = bot.get_channel(int(jdata['Welcome_channel']))
    await channel.send(f'{members} join!')

# 成員離開
@bot.event
async def on_member_remove(members):
    channel = bot.get_channel(int(jdata['Leave_channel']))
    await channel.send(f'{members} leave!')

# <---------- 傳送訊息 ---------->
# 顯示機器人延遲 指令
@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} (ms)')

# <---------- 圖片 ---------->
# 傳送本機圖片
@bot.command()
async def 圖片(ctx):
    pic = discord.File(jdata['pic'])
    await ctx.send(file = pic)

# 隨機傳送本機圖片
@bot.command()
async def 隨機圖片(ctx):
    random_pic = random.choice(jdata['pic'])
    pic = discord.File(random_pic)
    await ctx.send(file = pic)

# 隨機傳送圖片網址
@bot.command()
async def web(ctx):
    random_pic = random.choice(jdata['url_pic'])
    await ctx.send(random_pic)

# 啟動 bot
bot.run(jdata['TOKEN'])