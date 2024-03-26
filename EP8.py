# Embed 嵌入訊息
# --> cmds / main.py

# https://cog-creators.github.io/discord-embed-sandbox/

import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime

class Main(Cog_Extension):
    # Embed 嵌入訊息
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

async def setup(bot):
    await bot.add_cog(Main(bot))