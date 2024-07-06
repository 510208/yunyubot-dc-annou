# ❤ 協助開發

非常感謝你願意協助本專案的開發，我由衷地感謝你！

為本專案開發作貢獻是一件非常簡單的事，請照著以下貢獻的方法與規則操作！

## 🍽️ 建立分支

在為專案開發時，請位你的編輯建立一個分支。以下是不錯的分支名稱建議：

- **add-yaml-configure**：提及你的更新內容為協助建立YAML配置文件
- **randomgames**：提及你的更新內容與一些小遊戲有關係

以下是不好的範例
- **master**：與常用於主要分支的內容重複，容易造成歧義
- **add-some-game-for-some-players**：太長，不容易理解

請將你所有的更新、貢獻與修改新增在你建立的分支中，不要提交到任何不相干的分支。並且在Pull Requst提交時請求合併你的分支，而非主要的main分支

> [!CAUTION]
> 不要提交任何變更到main分支，我不會為該分支的內容進行審核與研究。也不要在最後提交完成後再啟動開發分支，否則我也可能不進行處理或略過

## 🧩 製作擴充工具

### Python 檔案規定

本專案採用 Discord.py 做開發，並使用 Cogs 架構保證專案的順暢與穩定。如果你想為機器人做更多擴充功能，請使用以下 Python Cogs 模板：

```python
# <擴充功能名稱>擴充功能

import discord
from discord.ext import commands
from discord import app_commands
import logging
import yaml

with open('cfg.yml', "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)

logger = logging.getLogger(__name__)

class MyExtension(commands.Cog):
    # ...
    pass

async def setup(bot):
    await bot.add_cog(MyExtension(bot))
    logger.info("MyExtension 已經註冊")
```

開發過程中請依照以下規定，以保證專案與擴充功能的一體性：

- 名稱（模板中的`MyExtension`）請記得替換
- `import`請全部置放在最上方，不要放在函式、Class或其他物件中
- 請保證程式碼的可讀性，不要為變數、陣列或其他項目加密
- 請保留一定的空間，讓使用者可以配置
- 配置請新增在`cfg.yml`中，不要自行新增其他文件
- 如果需要其他 Python Module，請記得寫進`requirements.txt`中
- 請在適當的地方撰寫註解，方便其他人閱讀
- 請盡力而為，我們感激你的貢獻！

### 配置檔規定

為了維持簡單的操作，請將配置項目安放在`cfg.yml`中，將以下代碼添加在配置檔最下方：

```yaml
# ================================
#  ○ <你模組的名稱>設定
#  齒輪：<你模組的檔名>.py
# ================================
#
myextension:
  # 啟用
  enabled: true

  # ...
```

麻煩依照以下說明設計，以維持專案一體性：

- 配置檔的鍵名要有意義，請避免使用如`a`、`b`等無意義的鍵名
- 請留下足夠的彈性給使用者，他們會很感激你的！
- 請將上方的內容改成適合自己的
- 請為配置鍵撰寫適合的註解，如果有 Placeholder 也請說明之
- 預設值要有意義，不要亂寫

再次感謝，謝謝您的幫忙！

### 為擴充功能編寫說明

請記得在寫完程式後做以下幾件事：

1. 在`readme.md`中，備註與謝誌位置主動放上你的大名，與你協助的內容，謝謝！（不填寫我們會協助填寫，不希望出現在上面請在PR告知）
2. 手動在 ExtGuide 資料夾建立一個`你擴充功能檔名.md`的檔案用以撰寫你擴充功能的說明
3. 如果你的擴充功能不需要預設啟動，或希望使用者自行決定是否啟動，請在檔名前加上`nl`兩字
4. 如果你不知道讀我檔案可以放什麼，可以使用以下範本：

```markdown
# 我的擴充功能

## ⓘ 關於擴充功能

- **作者**：SamHacker
- **授權條款**：GNU/GPL v3

## ⚙️ 配置

\```
# ================================
#  ○ <你模組的名稱>設定
#  齒輪：<你模組的檔名>.py
# ================================
#
myextension:
  # 啟用
  enabled: true

  # ...
\```

- `enabled`：啟用擴充功能
- ...
```

## 🏋️ Pull Request 規則

提出PR時請記得保持以下列舉的項目，我們會很樂意為你審核：

- 請在[這裡](https://github.com/510208/yunyubot-dc-annou/pulls)提出PR
- 請簡述你協助製作的功能與需要的資訊
- 如果你先前有提Issue做建議，也請附上Issue的連結
- 謝謝您的貢獻^^
