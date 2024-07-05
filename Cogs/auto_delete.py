# 公告頻道防多餘訊息擴充功能

import discord
from discord.ext import commands
from discord import app_commands
import logging
import yaml

with open('cfg.yml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

logger = logging.getLogger(__name__)

class Remove_Message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        logger.info("Remove Message cog 已經載入")

    # 事件
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.channel.id in config['auto_delete']['channel_id'] and \
            message.author.id not in config['auto_delete']['whitelist'] and \
                config['auto_delete']['enabled']:
            if config['auto_delete']['dm']:
                await message.author.send(config['auto_delete']['dm_message'])
            await message.delete()

def setup(bot):
    bot.add_cog(Remove_Message(bot))
    logger.info("Welcome cog 已經註冊")