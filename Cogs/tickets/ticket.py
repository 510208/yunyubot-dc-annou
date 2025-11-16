import asyncio
import json
import logging
import os
import discord
from discord.ext import commands
from discord import app_commands
import yaml
import json

logger = logging.getLogger(__name__)

with open('config.yml', "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)["tickets"]
    message = config["messages"]
    multiline_msg = config["multiline_messages"]
    button_texts = config["button_texts"]
    embed_txt = config["embed_text"]

SELF_PATH = os.path.dirname(os.path.abspath(__file__))
os.chdir(SELF_PATH)
FILE_PATH = os.path.join(SELF_PATH, "data.json")
# 讀取 data.json
if not os.path.exists(FILE_PATH):
    logger.warning("找不到 data.json，正在建立新的 data.json")
    # 取得這個 Cog 所在的目錄，而非 main.py
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump({
            "ticket_panel_message_id": None
        }, file, indent=4)
    logger.info("已建立新的 data.json")

with open('data.json', "r", encoding="utf-8") as file:
    data = json.load(file)

COG_INTRO = {
    "name": "客服單系統",
    "description": "為伺服器新增客服單功能，由夜間部設計",
    "author": "SamHacker",
    "countributors": ["SamHacker", "!夜間部（woodypegasus_tw）"],
}

class MainMenu(discord.ui.View):
    # 主選單（建立客服單按鈕）
    def __init__(self, bot, timeout = None):
        super().__init__(timeout = timeout)
        self.bot = bot
    
    @discord.ui.button(
        label = button_texts["new_ticket"],
        style = discord.ButtonStyle.primary,
        custom_id = "ticket-on:on_button",
        emoji = "🎫"
    )
    async def on_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        """建立一個以'ticket-{username}'為名的新頻道"""
        # 設定相關常數
        TICKET_CATEGORY = config["category_id"]   # 客服單分類的 ID
        GUILD = interaction.guild
        AUTHOR = interaction.user
        STAFF_ROLE_ID: list[int] = config["staff_role_id"]
        # 檢查是否已經有相同名稱的頻道
        for channel in GUILD.text_channels:
            if channel.name == f"ticket-{AUTHOR.name}":
                await interaction.response.send_message(
                    message["ticket_exists"],
                    ephemeral = True
                )
                return
        
        try:
            # 建立新頻道
            overwrites = {
                GUILD.default_role: discord.PermissionOverwrite(read_messages=False),  # 禁止所有人查看
                interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages=True),  # 允許用戶查看
                GUILD.me: discord.PermissionOverwrite(read_messages=True, send_messages=True),  # 允許機器人查看
            }
            # 遍覽所有客服人員的 ID，並將其加入到 overwrites 中
            for role_id in STAFF_ROLE_ID:
                role = GUILD.get_role(role_id)
                overwrites[role] = discord.PermissionOverwrite(read_messages=True, send_messages=True)
            
            CHANNEL = await GUILD.create_text_channel(
                f"ticket-{AUTHOR.name}",
                category = GUILD.get_channel(TICKET_CATEGORY),
                overwrites = overwrites
            )

            # 發送歡迎訊息
            staff_mentions = ", ".join([GUILD.get_role(role_id).mention for role_id in STAFF_ROLE_ID])
            await CHANNEL.send(
                multiline_msg["welcome_ticket"].format(
                    user = AUTHOR.name,
                    user_mention = AUTHOR.mention,
                    user_id = AUTHOR.id,
                    channel = CHANNEL.name,
                    channel_mention = CHANNEL.mention,
                    channel_id = CHANNEL.id,
                    staff_mention = staff_mentions
                ),
                view = TicketView(self.bot)
            )
        except Exception as e:
            logger.error(f"建立客服單時發生錯誤：{e}")
            await interaction.response.send_message(
                message["error"],
                ephemeral = True
            )
        else:
            await interaction.response.send_message(
                f"你的客服單已創建：{CHANNEL.mention}",
                ephemeral = True
            )

class TicketConfirmClose(discord.ui.View):
    def __init__(self, bot, timeout = None):
        super().__init__(timeout = timeout)
        self.bot = bot

    async def send_log(self, interaction: discord.Interaction):
        """
        傳送 log 文件

        Parameters:
        interaction (discord.Interaction): 交互事件
        """
        messages = []
        async for message in interaction.channel.history(limit=None, oldest_first=True):
            messages.append(message)

        # 確保 history 目錄存在
        if not os.path.exists("./history"):
            os.makedirs("./history")

        # 將 messages 寫入到根目錄下的 log 文件，並記錄下該檔案，以便稍後傳送成附加檔案後移除
        FILE_NAME = f"./history/log-{interaction.channel.name}.txt"
        try:
            with open(FILE_NAME, "w", encoding="utf-8") as file:
                for message in messages:
                    file.write(f"{message.author.name} ({message.author.id}): {message.content}\n")
        except Exception as e:
            logger.error(f"寫入 log 文件時發生錯誤：{e}")
            return {"embed": None, "file": None, "status": False, "error": e}
        
        # 以二進位讀取模式打開文件並讀入進 discord.File 類型
        try:
            with open(FILE_NAME, "rb") as f:
                # 將 log 文件讀入為 discord.File 類型，以便稍後傳送
                file = discord.File(f, filename=FILE_NAME)
        except Exception as e:
            logger.error(f"讀取 log 文件時發生錯誤：{e}")
            return {"embed": None, "file": None, "status": False, "error": e}
        
        # 建立 Embed 訊息
        embed = discord.Embed(
            title="客服單已關閉",
            color=discord.Color.red(),
            description=f"客服單 {interaction.channel.name} 已關閉"
        )
        user_name = interaction.channel.name.split("-")[1]  # 取得客服單的用戶名稱
        user = interaction.guild.get_member_named(user_name)
        embed.add_field(name="開啟人員", value=f"<@{user.id}>", inline=True)

        # 傳送 log 文件至 config["log_channel_id"] 中
        log_channel = interaction.guild.get_channel(config["log_channel_id"])
        await log_channel.send(
            f"客服單 {interaction.channel.name} 已關閉",
            file=file
        )

        return {"embed": embed, "file": {"object": file, "path": FILE_NAME}, "status": True, "error": None}



    @discord.ui.button(
        label = button_texts["confirm"],
        style = discord.ButtonStyle.success,
        custom_id = "ticket-off:off_button"
    )
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        """確認關閉客服單"""
        # 設定相關常數
        GUILD = interaction.guild
        AUTHOR = interaction.user
        # 關閉客服單
        try:
            r = await self.send_log(interaction)
            if r["status"]:
                # 移除log文件
                try:
                    os.remove(r["file"]["path"])
                except Exception as e:
                    logger.error(f"刪除 log 文件時發生錯誤：{e}")
                # 刪除客服單頻道
                await interaction.channel.delete()
            else:
                await interaction.response.send_message(
                    message["error"],
                    ephemeral = True
                )
                await interaction.followup.send(
                    "若需要移除此客服單，請要求管理員手動刪除\n並請管理員檢視 log 文件以獲取更多資訊"
                )
        except Exception as e:
            logger.error(f"關閉客服單時發生錯誤：{e}")
            await interaction.response.send_message(
                message["error"],
                ephemeral = True
            )
        else:
            # await interaction.response.send_message(
            #     message["ticket_closed"],
            #     ephemeral = True
            # )
            pass

    @discord.ui.button(
        label = button_texts["cancel"],
        style = discord.ButtonStyle.danger,
        custom_id = "ticket-off:cancel_button"
    )
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        """取消關閉客服單"""
        # 把確認訊息刪除
        await interaction.response.edit_message(content="已取消關閉客服單", view=None)
        await interaction.message.delete()

class TicketView(discord.ui.View):
    # 客服單選單（關閉客服單按鈕）
    def __init__(self, bot, timeout = None):
        super().__init__(timeout = timeout)
        self.bot = bot

    # 關閉客服單按鈕
    @discord.ui.button(
        label = button_texts["close_ticket"],
        style = discord.ButtonStyle.danger,
        custom_id = "ticket-off:off_button"
    )
    async def off_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        """關閉客服單"""
        # 設定相關常數
        GUILD = interaction.guild
        AUTHOR = interaction.user
        # 檢查是否為客服單頻道
        if not interaction.channel.name.startswith("ticket-"):
            await interaction.response.send_message(
                message["error"],
                ephemeral = True
            )
            return
        
        # 傳送確認訊息
        confirm_view = TicketConfirmClose(self.bot, timeout=config["confirm_message_expired"])
        await interaction.response.send_message(
            message["close_ticket_confirm"],
            view = confirm_view,
            ephemeral = True
        )

    # 呼叫客服人員按鈕
    @discord.ui.button(
        label = button_texts["call_staff"],
        style = discord.ButtonStyle.primary,
        custom_id = "ticket-call:call_button"
    )
    async def call_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            GUILD = interaction.guild
            AUTHOR = interaction.user
            STAFF_ROLE_ID: list[int] = config["staff_role_id"]
            # 檢查是否為客服單頻道
            if not interaction.channel.name.startswith("ticket-"):
                await interaction.response.send_message(
                    message["error"],
                    ephemeral=True
                )
                return
            # 傳送呼叫訊息
            staff_mentions = ", ".join([GUILD.get_role(role_id).mention for role_id in STAFF_ROLE_ID])
            await interaction.response.send_message(
                multiline_msg["call_staff"].format(
                    user=AUTHOR.name,
                    user_mention=AUTHOR.mention,
                    user_id=AUTHOR.id,
                    channel=interaction.channel.name,
                    channel_mention=interaction.channel.mention,
                    channel_id=interaction.channel.id,
                    staff_mention=staff_mentions
                )
            )
            # 通知客服人員
            for role_id in STAFF_ROLE_ID:
                role = GUILD.get_role(role_id)
                for member in role.members:
                    await member.send(
                        multiline_msg["staff_notification"].format(
                            user=AUTHOR.name,
                            user_mention=AUTHOR.mention,
                            channel=interaction.channel.name,
                            channel_mention=interaction.channel.mention
                        )
                    )
        except Exception as e:
            logger.error(f"呼叫客服時發生錯誤：{e}")
            await interaction.response.send_message("發生錯誤：無法呼叫客服", ephemeral=True)

class ViewsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.add_view(MainMenu(bot, timeout=None))  # 添加持久化 View
        self.bot.add_view(TicketView(bot, timeout=None))  # 添加持久化 View

    # 傳送主選單
    tk = app_commands.Group(
        name = "ticket",
        description = "客服單功能"
    )
    
    # # 啟動時重啟持久化的按鈕
    # @commands.Cog.listener()
    # async def on_ready(self):
    #     logging.debug("客服單系統正在重啟持久化的按鈕")
    #     # 客服單頻道中重啟持久化的按鈕
    #     for guild in self.bot.guilds:
    #         for channel in guild.text_channels:
    #             logger.debug(f"正在檢查頻道：{channel.name}")
    #             if channel.name.startswith("ticket-"):
    #                 view = TicketView()
    #                 await channel.send(
    #                     embed = discord.Embed(
    #                         title = embed_txt["ticket_panel"]["title"],
    #                         color = discord.Color.green()
    #                     ),
    #                     view = view
    #                 )
    #                 logger.debug(f"已重啟 Persist View 於頻道：{channel.name}")

    #     # 主面板頻道中重啟持久化的按鈕
    #     # 取得主面板頻道
    #     main_channel = self.bot.get_channel(config["ticket_panel_id"])
    #     view = MainMenu()
    #     # 檢查是否有紀錄面板的訊息ID
    #     if data["ticket_panel_message_id"]:
    #         try:
    #             message = await main_channel.fetch_message(data["ticket_panel_message_id"])
    #         except discord.errors.NotFound:
    #             logger.warning("找不到主面板訊息，正在重新建立主面板訊息")
    #             embed = discord.Embed(
    #                 title = embed_txt["ticket_panel"]["title"],
    #                 description = embed_txt["ticket_panel"]["description"],
    #                 color = discord.Color.green()
    #             )
    #             message = await main_channel.send(embed = embed, view = view)
    #             data["ticket_panel_message_id"] = message.id
    #             with open("data.json", "w", encoding="utf-8") as file:
    #                 json.dump(data, file, indent=4)
    #             logger.info("已重新建立主面板訊息")
    #         except Exception as e:
    #             logger.error(f"重啟主選單中持久化按鈕時發生錯誤：{e}")
    #         else:
    #             await message.edit(
    #                 embed = discord.Embed(
    #                     title = embed_txt["ticket_panel"]["title"],
    #                     color = discord.Color.green()
    #                 ),
    #                 view = view
    #             )
    #             logger.debug("已重啟 Persist View 於主面板頻道")
    #     else:
    #         logger.warning("找不到主面板訊息，正在重新建立主面板訊息")
    #         embed = discord.Embed(
    #             title = embed_txt["ticket_panel"]["title"],
    #             description = embed_txt["ticket_panel"]["description"],
    #             color = discord.Color.green()
    #         )
    #         message = await main_channel.send(embed = embed, view = view)
    #         data["ticket_panel_message_id"] = message.id
    #         with open("data.json", "w", encoding="utf-8") as file:
    #             json.dump(data, file, indent=4)
    #         logger.info("已重新建立主面板訊息")

    @tk.command(
        name = "panel",
        description = "顯示客服單主選單"
    )
    async def panel(self, ctx):
        """顯示客服單主選單"""
        # 移除舊的訊息
        if data["ticket_panel_message_id"]:
            try:
                message = await ctx.channel.fetch_message(data["ticket_panel_message_id"])
                await message.delete()
            except discord.errors.NotFound:
                logger.warning("找不到主面板訊息，正在重新建立主面板訊息")
            except Exception as e:
                logger.error(f"刪除主面板訊息時發生錯誤：{e}")
        # 顯示新的訊息
        view = MainMenu()
        embed = discord.Embed(
            title = embed_txt["ticket_panel"]["title"],
            description = embed_txt["ticket_panel"]["description"],
            color = discord.Color.green()
        )
        message = await ctx.send(embed = embed, view = view)
        data["ticket_panel_message_id"] = message.id
        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        logger.info("已重新建立主面板訊息")
    
    @tk.command(
        name = "close",
        description = "關閉客服單"
    )
    async def close(self, ctx):
        """關閉客服單"""
        view = TicketView()
        await ctx.send(
            embed = discord.Embed(
                title = embed_txt["reopen_ticket"],
                color = discord.Color.green()
            ),
            view = view
        )

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info(f"{COG_INTRO['name']} 已經載入")
        # 自動刪除 history 目錄下的 log 文件
        if not config["remove_log_when_bot_launch"]:
            return
        try:
            for file in os.listdir("./history"):
                os.remove(f"./history/{file}")
        except Exception as e:
            logger.error(f"刪除 log 文件時發生錯誤：{e}")

async def setup(bot):
    if not config["enabled"]:
        logger.info("載入客服單系統失敗，原因：在配置文件中停用了此模組")
        return
    await bot.add_cog(ViewsCog(bot))
    logger.info(f"{COG_INTRO['name']} 已經註冊")