import discord
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='[', intents=intents)

@bot.event
async def on_ready():
    print('>> bot is online <<')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} (ms)')

bot.run('MTE4ODExNDg3NDExMTM2MTEwNQ.GTJgOR.uP8-f688QG_z5XSVwHxttI3zPokl3kacLaweLg')