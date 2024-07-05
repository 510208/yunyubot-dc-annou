# 關於

import discord
from discord.ext import commands
from discord import app_commands
import discord.ui as ui
import yaml
import logging
from main import BOT_ADMIN
from nltemplates import *
import re
import datetime

logger = logging.getLogger(__name__)

COG_INTRO = {
    "name": "公告系統",
    "description": "用於公告設定的擴充功能"
}

# 讀取設定檔
with open("cfg.yml", "r", encoding="utf-8") as file:
    cfg = yaml.safe_load(file)

class About(commands.Cog):
    @app_commands.command(name='關於')
    async def about(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title = "關於",
            description = "這是雲羽生存服專用的機器人\n由插件師兼伺服器工程師SamHacker搭建",
            color = 0x00ff00
        )
        embed.add_field(
            name = "作者",
            value = "SamHacker"
        )
        embed.add_field(
            name = "版本",
            value = "1.0.0"
        )
        embed.add_field(
            name = "授權條款",
            value = "GNONE GNU General Public License v3.0"
        )
        embed.add_field(
            name = "原始碼",
            value = "[GitHub](https://github.com/510208/yunyubot-dc-annou)"
        )
        # 設定大頭貼
        embed.set_thumbnail(url="https://gravatar.com/avatar/f7598bd8d4aba38d7219341f81a162fc842376b3b556b1995cbb97271d9e2915?s=256")
        # 設定頁尾
        embed.set_footer(text="© 2021 SamHacker")
        # 附加一張圖片，位置在main.py的同一層目錄下resources資料夾中
        file = discord.File("resources/cover.png", filename="cover.png")
        embed.set_image(url="attachment://cover.png")
        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(About(bot))