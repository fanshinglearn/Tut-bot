import discord
from discord.ext import commands

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

# 成員加入
@bot.event
async def on_member_join(members):
    channel = bot.get_channel(1217763083288580136)
    await channel.send(f'{members} join!')

# 成員離開
@bot.event
async def on_member_remove(members):
    channel = bot.get_channel(1217763163378810890)
    await channel.send(f'{members} leave!')

# 顯示機器人延遲 指令
@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} (ms)')

# 啟動 bot
bot.run('MTE4ODExNDg3NDExMTM2MTEwNQ.GTJgOR.uP8-f688QG_z5XSVwHxttI3zPokl3kacLaweLg')