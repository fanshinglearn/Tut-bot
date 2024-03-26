# 訊息複誦、清理訊息
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime

class Main(Cog_Extension):
    @commands.command()
    async def sayd(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)
    
    @commands.command()
    async def clean(self, ctx, num:int):
        await ctx.channel.purge(limit=num+1)

async def setup(bot):
    await bot.add_cog(Main(bot))