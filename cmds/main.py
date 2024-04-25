import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime

class Main(Cog_Extension):
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} (ms)')
    
    @commands.command()
    async def hi(self, ctx):
        await ctx.send('HELLO')
        await ctx.send('<@511899806826758148>')
    
    @commands.command()
    async def em(self, ctx):
        embed=discord.Embed(title="op.gg", url="https://www.op.gg/", description="lol", color=0x4596bf,
                            timestamp=datetime.datetime.now())
        embed.set_author(name="fanshing", icon_url="https://lh3.googleusercontent.com/-JfyMf7Wf_tboP30yAhPOxFUmULHpj55RGXVoSHpSzMoVJIBYtAntWmmkpu37dpYFSP6Dm6FwJoY7dGwQ8Ec3zEgvu8ZAO-H9nbbIAlt81oD1Q4tOMfU=h60")
        embed.set_thumbnail(url="https://lh3.googleusercontent.com/-JfyMf7Wf_tboP30yAhPOxFUmULHpj55RGXVoSHpSzMoVJIBYtAntWmmkpu37dpYFSP6Dm6FwJoY7dGwQ8Ec3zEgvu8ZAO-H9nbbIAlt81oD1Q4tOMfU=h60")
        embed.add_field(name="中飛妮可", value="隨機單中", inline=False)
        embed.add_field(name="2", value="222", inline=False)
        embed.add_field(name="3", value="333", inline=False)
        embed.add_field(name="4", value="444", inline=False)
        embed.set_footer(text="嬰兒")
        await ctx.send(embed=embed)
    
    @commands.command()
    async def sayd(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)
    
    @commands.command()
    async def clean(self, ctx, num:int):
        await ctx.channel.purge(limit=num+1)


async def setup(bot):
    await bot.add_cog(Main(bot))