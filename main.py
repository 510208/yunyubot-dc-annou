import discord
import logging
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import os
import json
import asyncio
from sympy import epath

# Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(lineno)d: [%(asctime)s][%(levelname)s] - [%(module)s] %(message)s'
)

# 可以使用指令的使用者ID
BOT_ADMIN = [
    "959977374471028779",
    959977374471028779
]

# Bot
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# Cogs Slash Command
@bot.event
async def on_ready():
    logging.info(f'Logged in as {bot.user} (ID: {bot.user.id})')
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
    cogs = []
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            cogs.append(filename[:-3])
        
    # 取出已啟用的Cogs
    enabled_cogs = []
    for cog in cogs:
        if cog in bot.cogs:
            enabled_cogs.append(cog)
    
    # 回傳Embed訊息
    embed = discord.Embed(
        title='Cogs列表',
        description='以下為所有Cogs列表',
        color=discord.Color.blue()
    )
    embed.add_field(
        name='已啟用',
        value='\n'.join(enabled_cogs) if enabled_cogs else '無'
    )
    embed.add_field(
        name='未啟用',
        value='\n'.join([cog for cog in cogs if cog not in enabled_cogs]) if cogs else '無'
    )
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
    try:
        # 檢查是否有該Cog
        if cog not in bot.cogs:
            await ctx.response.send_message('找不到該Cog')
            return
        
        # 啟用Cog
        bot.load_extension(f'cogs.{cog}')
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
        if cog not in bot.cogs:
            await ctx.response.send_message('找不到該Cog')
            return
        
        # 停用Cog
        bot.unload_extension(f'cogs.{cog}')
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
        if cog not in bot.cogs:
            await ctx.response.send_message('找不到該Cog')
            return
        
        # 重新載入Cog
        bot.reload_extension(f'cogs.{cog}')
        await ctx.response.send_message(f'已重新載入{cog}')
    except Exception as e:
        logging.error(f'發生錯誤：{e}')
        await ctx.response.send_message(f'發生錯誤：{e}')

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if message.user.id not in BOT_ADMIN:
        await message.channel.send('你沒有權限使用此機器人', ephemeral=True)
        return
    if message.content.startswith('sh!'):
        cmd = message.content.split('!')[1]
        if cmd == 'sync':
            syncedcmd = await bot.tree.sync()
            await message.channel.send(f'✅ 同步指令成功！\n{syncedcmd}', ephemeral=True)
            return
        
# 一開始bot開機需載入全部程式檔案
async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

# Start Bot
with open('token.txt', 'r') as f:
    token = f.readline()
    logging.info('讀取Token成功！')
    # logging.info(token)

async def main():
    async with bot:
        await load_extensions()
        await bot.start(token)

# 確定執行此py檔才會執行
if __name__ == "__main__":
    asyncio.run(main())