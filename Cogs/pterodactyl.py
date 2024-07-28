# Pterodactyl 遊戲內輔助功能

import discord
from discord.ext import commands
from discord import app_commands
import logging
import yaml
from pydactyl import PterodactylClient

with open('cfg.yml', "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)["pterodactyl"]

logging.getLogger('pydactyl').setLevel(logging.INFO)
logger = logging.getLogger(__name__)

class PteroManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        logger.info("Pterodactyl 已經載入")

    pt = app_commands.Group(
        name = "Pterodactyl",
        description = "Pterodactyl 遊戲內輔助功能"
    )

    # 定義電源選項相關
    pwr = app_commands.Group(
        name = "電源管理",
        description = "電源管理",
        parent=pt
    )
    @pwr.command(
        name = "開機",
        description = "開啟伺服器",
    )
    async def start(self, ctx: discord.Interaction):
        await ctx.response.send_message("開啟伺服器")

async def setup(bot):
    if not(config["enabled"]):
        logger.info("載入 Pterodactyl 模組失敗，原因：在配置文件中停用了此模組")
        return
    await bot.add_cog(PteroManager(bot))
    logger.info("Pterodactyl 已經註冊")