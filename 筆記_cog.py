# < ---------- cmds ---------->
import discord
from discord.ext import commands

# 繼承 core.classes.py 的 __init__
from core.classes import Cog_Extension

# 繼承 Cog_Extension
class Main(Cog_Extension):
    # @bot.command() 改為 @commands.command()
    @commands.command()
    # 加入 self
    async def hi(self, ctx):
        await ctx.send('HELLO')

# 主程式呼叫 setup 傳入 bot 給 Main class
# 新版本 discore.py 似乎需要加入 async 和 await
async def setup(bot):
    await bot.add_cog(Main(bot))

# 主程式
import discord
from discord.ext import commands
import os
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='[', intents=intents)

@bot.event
async def on_ready():
    # 新版本 discord.py 似乎需要寫成一個 async 函式 使用 await 呼叫
    await load_extensions()
    print('>> bot is online <<')

# load
@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')

# unload
@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Un - Loaded {extension} done.')

# reload
@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re - Loaded {extension} done.')

# 新版本 discord.py 似乎需要寫成一個 async 函式
async def load_extensions():
    for filename in os.listdir('./cmds'):
        if filename.endswith('.py'):
            # 加 await
            await bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == '__main__':
    bot.run(jdata['TOKEN'])