import discord
import logging
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import os
import yaml
import asyncio
import platform

# Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(lineno)d: [%(asctime)s][%(levelname)s] - [%(module)s] %(message)s'
)
logging.getLogger('discord').setLevel(logging.INFO)

with open('cfg.yml', 'r', encoding='utf-8') as f:
    cfg = yaml.load(f, Loader=yaml.FullLoader)
    logging.info('讀取cfg.yml成功！')
# 檢查錯誤狀態
if cfg is None:
    logging.error('cfg.yml為空！')
    exit()

# 可以使用指令的使用者ID
BOT_ADMIN = cfg["admin_id"]

# Bot
bot = commands.Bot(command_prefix='sh!', intents=discord.Intents.all())

# Cogs Slash Command
@bot.event
async def on_ready():
    ASCII_CODE = f"""
____________________________________________________

         \   /|  |
          \ / |  |  Logged in as {bot.user}
           T  |  |  Bot ID: {bot.user.id}
           |  \__/
____________________________________________________

  OS: {platform.system()} {platform.release()}
  Python Version: {platform.python_version()}
  Discord.py Version: {discord.__version__}
  Development by 510208, Thanks for using!

"""
    for line in ASCII_CODE.split('\n'):
        logging.info(line)
    logging.info('------')
    for guild in bot.guilds:
        logging.info(f'{guild.name} (ID: {guild.id})')
    logging.info('------')
    await bot.change_presence(activity=discord.Game(name='正在雲羽生存服搞事...'))
    logging.info('同步指令中...')
    slash = await bot.tree.sync()
    if slash:
        logging.info(f'指令同步完成：{slash}')
    else:
        logging.error('指令同步失敗')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        ctx.send('欸欸指令不存在', ephemeral=True)
        return
    raise error

@bot.tree.command(
    name='齒輪列表',
    description='列出所有Cogs資料夾中的Cogs'
)
async def cog_list(ctx):
    if ctx.user.id not in BOT_ADMIN:
        await ctx.response.send_message('你沒有權限使用此機器人', ephemeral=True)
        return
    # 遍覽Cogs資料夾，並取出所有可用Cogs，然後逐一檢查是否被啟用
    logging.info('取得Cogs列表')
    logging.info(f'請求發起人：{ctx.user}')
    # cogs = []
    # for filename in os.listdir('./cogs'):
    #     if filename.endswith('.py'):
    #         cogs.append(filename[:-3])
        
    # 取出已啟用的Cogs
    # enabled_cogs = []
    # for cog in cogs:
    #     if cog in bot.cogs:
    #         enabled_cogs.append(cog)
    
    # 回傳Embed訊息
    embed = discord.Embed(
        title='Cogs列表',
        description='以下為所有Cogs列表',
        color=discord.Color.blue()
    )
    logging.info(f'已啟用的Cogs：{bot.cogs}')
    for cog in bot.cogs:
        embed.add_field(
            name=cog,
            value='<:check:1254019091371397130> 已啟用',
            inline=False
        )
    # 取得bot.cogs的所有鍵名（bot.cogs是一個字典）
    all_cogs = bot.cogs.keys()
    # 將all_cogs全部變小寫
    all_cogs = [cog.lower() for cog in all_cogs]
    for cog in os.listdir('./Cogs'):
        if cog.endswith('.py'):
            if cog[:-3] not in all_cogs:
                embed.add_field(
                    name=cog[:-3],
                    value='<:dangerous:1254019093900558397> 未啟用',
                    inline=False
                )
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Engranajesreductores.JPG/240px-Engranajesreductores.JPG")
    await ctx.response.send_message(embed=embed)

@bot.tree.command(
    name='啟用齒輪',
    description='啟用指定的Cog'
)
async def enable_cog(ctx, cog: str):
    logging.info('啟用Cogs')
    logging.info(f'請求發起人：{ctx.user}, 參數： cog={cog}')
    if ctx.user.id not in BOT_ADMIN:
        await ctx.response.send_message('你沒有權限使用此機器人', ephemeral=True)
        return
    # if cog == '*':
    #     # 先卸載全部Cog
    #     for cog in bot.cogs:
    #         await bot.unload_extension(f'Cogs.{cog}')
    #     # 啟用全部Cog
    #     await load_extensions()
    try:
        # 檢查是否有該Cog
        if os.path.isfile(f'./Cogs/{cog}.py') == False:
            await ctx.response.send_message('找不到該Cog')
            return
        # 啟用Cog
        await bot.load_extension(f'Cogs.{cog}')
        await ctx.response.send_message(f'已啟用{cog}')
    except Exception as e:
        logging.error(f'發生錯誤：{e}')
        await ctx.response.send_message(f'發生錯誤：{e}')

@bot.tree.command(
    name='停用齒輪',
    description='停用指定的Cog'
)
async def disable_cog(ctx, cog: str):
    logging.info('停用Cogs')
    logging.info(f'請求發起人：{ctx.user}, 參數： cog={cog}')
    if ctx.user.id not in BOT_ADMIN:
        await ctx.response.send_message('你沒有權限使用此機器人', ephemeral=True)
        return
    try:
        # 檢查是否有該Cog
        if os.path.isfile(f'./Cogs/{cog}.py') == False:
            await ctx.response.send_message('找不到該Cog')
            return
        
        # 停用Cog
        await bot.unload_extension(f'Cogs.{cog}')
        await ctx.response.send_message(f'已停用{cog}')
    except Exception as e:
        logging.error(f'發生錯誤：{e}')
        await ctx.response.send_message(f'發生錯誤：{e}')

@bot.tree.command(
    name='重新載入齒輪',
    description='重新載入指定的Cog'
)
async def reload_cog(ctx, cog: str):
    logging.info('熱重載Cogs')
    logging.info(f'請求發起人：{ctx.user}, 參數： cog={cog}')
    if ctx.user.id not in BOT_ADMIN:
        await ctx.response.send_message('你沒有權限使用此機器人', ephemeral=True)
        return
    try:
        # 檢查是否有該Cog
        if os.path.isfile(f'./Cogs/{cog}.py') == False:
            await ctx.response.send_message('找不到該Cog')
            return
        
        # 重新載入Cog
        await bot.reload_extension(f'Cogs.{cog}')
        await ctx.response.send_message(f'已重新載入{cog}')
    except Exception as e:
        logging.error(f'發生錯誤：{e}')
        await ctx.response.send_message(f'發生錯誤：{e}')

@bot.tree.command(
    name='說明',
    description='取得機器人指令的說明'
)
async def help(ctx):
    logging.info('取得指令說明')
    logging.info(f'請求發起人：{ctx.user}')
    embed = discord.Embed(
        title='指令說明',
        description='以下為機器人指令的說明',
        color=discord.Color.green()
    )
    for command in bot.tree.walk_commands():
        embed.add_field(
            name=command.name,
            value=command.description,
            inline=False
        )
    await ctx.response.send_message(embed=embed)

@bot.command(
    name='sync',
    description='同步指令'
)
async def sync(ctx):
    logging.info('同步指令中...')
    if ctx.author.id not in BOT_ADMIN:
        await ctx.send('你沒有權限使用此機器人')
        return
    mes = await ctx.send('同步指令中...')
    slash = await bot.tree.sync()
    if not slash:
        await ctx.send('指令同步失敗')
        return
    embed = discord.Embed(
        title='指令同步',
        description='指令同步完成',
        color=discord.Color.green()
    )
    for slash_sl in slash:
        name = slash_sl.name
        description = slash_sl.description
        embed.add_field(
            name=name,
            value=description,
            inline=False
        )
    embed.set_thumbnail(url="https://gravatar.com/avatar/f7598bd8d4aba38d7219341f81a162fc842376b3b556b1995cbb97271d9e2915?s=256")
    # 正確的調用方式
    await mes.edit(content="完成同步！", embed=embed)

# 一開始bot開機需載入全部程式檔案
async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py") and not(filename.startswith("nl")):
            try:
                logging.info(f"載入{filename}中...")
                await bot.load_extension(f"Cogs.{filename[:-3]}")
                logging.info(f"載入{filename}成功")
                logging.getLogger(f'Cogs.{filename}').setLevel(logging.INFO)
            except Exception as e:
                logging.error(f"載入{filename}失敗：{e}")
                continue
        else:
            if filename.startswith("nl"):
                logging.info(f"跳過{filename}, 原因：採用nl方式跳過載入")
            else:
                logging.info(f"跳過{filename}")

# Start Bot
with open('token.txt', 'r') as f:
    token = f.readline()
    logging.info('讀取Token成功！')
    # logging.info(token)

async def main():
    async with bot:
        await load_extensions()
        try:
            await bot.start(token)
        except KeyboardInterrupt:
            await bot.close()
            logging.info('Bot已關閉，謝謝使用！')
            exit(0)
        except discord.LoginFailure as e:
            logging.error('登入失敗，可能是Token錯誤')
            logging.error('請前往 https://github.com/510208/yunyubot-dc-annou/?tab=readme-ov-file#token%E9%8C%AF%E8%AA%A4 了解更多')
            logging.error(f'錯誤訊息：{e}')
        except discord.errors.RateLimited as e:
            logging.error('登入失敗，可能是登入次數過多')
            logging.error('請稍後再試')
            logging.error(f'錯誤訊息：{e}')
        except discord.errors.PrivilegedIntentsRequired as e:
            logging.error('登入失敗，可能是未開啟Privileged Gateway Intents')
            logging.error('請前往 https://github.com/510208/yunyubot-dc-annou/?tab=readme-ov-file#%E7%89%B9%E6%AC%8A%E7%B6%B2%E9%97%9C%E6%84%8F%E5%9C%96%E9%8C%AF%E8%AA%A4 了解更多')
            logging.error(f'錯誤訊息：{e}')
        except Exception as e:
            logging.error(f'Bot發生錯誤：{e}')
            logging.error('請前往 https://github.com/510208/yunyubot-dc-annou/?tab=readme-ov-file#-%E9%81%87%E5%88%B0%E5%95%8F%E9%A1%8C 回報錯誤')

# 確定執行此py檔才會執行
if __name__ == "__main__":
    asyncio.run(main())