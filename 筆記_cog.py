# < ---------- cmds ---------->
import discord
from discord.ext import commands
import datetime

# 繼承 core.classes.py 的 __init__
from core.classes import Cog_Extension

# 繼承 Cog_Extension
class Main(Cog_Extension):
    # @bot.command() 改為 @commands.command()
    @commands.command()
    # 加入 self
    async def hi(self, ctx):
        await ctx.send('HELLO')
    
    # on... 要用 @commands.Cog.listener()
    @commands.Cog.listener()
    # on_message()
    async def on_message(self, msg):
        # 各種變化
        keyword = ['apple', 'pen', 'pie', 'abc']
        # if msg.content == 'apple':
        # if msg.content.endswith('apple'):
        # 加入 msg.author != self.bot.user 可讓 bot 不陷入無限迴圈
        # if msg.content == 'apple' and msg.author != self.bot.user:
        if msg.content in keyword and msg.author != self.bot.user:
            await msg.channel.send('apple')
    
    # Embed 嵌入訊息
    @commands.command()
    async def em(self, ctx):
        embed=discord.Embed(title="op.gg", url="https://www.op.gg/", description="lol", color=0x4596bf,
                            # 時間截
                            timestamp=datetime.datetime.now())
        embed.set_author(name="fanshing", icon_url="https://lh3.googleusercontent.com/-JfyMf7Wf_tboP30yAhPOxFUmULHpj55RGXVoSHpSzMoVJIBYtAntWmmkpu37dpYFSP6Dm6FwJoY7dGwQ8Ec3zEgvu8ZAO-H9nbbIAlt81oD1Q4tOMfU=h60")
        embed.set_thumbnail(url="https://lh3.googleusercontent.com/-JfyMf7Wf_tboP30yAhPOxFUmULHpj55RGXVoSHpSzMoVJIBYtAntWmmkpu37dpYFSP6Dm6FwJoY7dGwQ8Ec3zEgvu8ZAO-H9nbbIAlt81oD1Q4tOMfU=h60")
        embed.add_field(name="中飛妮可", value="隨機單中", inline=False)
        embed.add_field(name="2", value="222", inline=False)
        embed.add_field(name="3", value="333", inline=False)
        embed.add_field(name="4", value="444", inline=False)
        embed.set_footer(text="嬰兒")
        await ctx.send(embed=embed)
    
    # 訊息複誦
    @commands.command()
    # * 會把因為空格分成 list 的一起傳
    async def sayd(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)
    
    # 清理訊息
    @commands.command()
    # 通常函數命名為 purge
    # 註解 num:int 就不用再轉換成 int
    async def clean(self, ctx, num:int):
        # 因傳送 [clean 3 也算一則訊息，需 +1
        await ctx.channel.purge(limit=num+1)


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