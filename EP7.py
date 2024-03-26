# on_message 關鍵字觸發
# --> cmds / event.py

import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, members):
        channel = self.bot.get_channel(int(jdata['Welcome_channel']))
        await channel.send(f'{members} join!')

    @commands.Cog.listener()
    async def on_member_remove(self, members):
        channel = self.bot.get_channel(int(jdata['Leave_channel']))
        await channel.send(f'{members} leave!')
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        keyword = ['apple', 'pen', 'pie', 'abc']
        # if msg.content == 'apple':
        # if msg.content.endswith('apple'):
        # if msg.content == 'apple' and msg.author != self.bot.user:
        if msg.content in keyword and msg.author != self.bot.user:
            await msg.channel.send('apple')

async def setup(bot):
    await bot.add_cog(Event(bot))