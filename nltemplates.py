import datetime
import yaml
import logging

logger = logging.getLogger(__name__)

with open('config.yml', 'r', encoding='utf-8') as f:
    cfg = yaml.load(f, Loader=yaml.FullLoader)
    logger.info('讀取config.yml成功！')

class UpdateMsgGen():
    def __init__(
        self,
        intro: str = """
太棒了！我們伺服器又更新了~~
快來看看這次我們又更新了些啥吧，快點喔！
""",
        content: list = [
            "新增了一個指令",
            "修復了一些錯誤",
            "更新了一些內容"
        ],
        starter: str = "959977374471028779"
    ):
        self.intro = intro
        # 將content轉換成字串，並在字串前方加上減號與空格使其可以直接放入markdown中
        self.content = "\n".join([f"- {i}" for i in content])
        # 利用datetime將當前時間轉換成UNIX時間戳（字串）
        self.timestamp = str(round(datetime.datetime.now().timestamp()))
        self.starter = starter
#         self.text = f"""
# ## 雲羽更新

# {self.intro}

# ### 更新內容
# {self.content}


# 最後，祝各位 **<:gousthappy:1194802726442381312>在本服中遊玩愉快！**
# 期待各位的新進度，掰掰！

# 📢 雲羽生存服 管理團隊 - <@{self.starter}> 敬上
#    <t:{self.timestamp}:F>

# [ ||<@&1190290928112517212>||  |  ||<@&1190291336750960773>||  |  ||<@&1190298140692185128>||  |  ||<@&1186541054514704434>||]
# """
        try:
            self.text = cfg["update_format"].format(
                intro=self.intro,
                content=self.content,
                timestamp=self.timestamp,
                starter=self.starter
            )
        # 在格式化中找不到佔位符時會報錯，這時就回報錯誤
        except KeyError:
            logger.warning("找不到佔位符，將使用預設訊息")
            self.text = f"""
## 伺服器更新

{self.intro}

### 更新內容
{self.content}


最後，祝各位 **<:gousthappy:1194802726442381312>在本服中遊玩愉快！**
期待各位的新進度，掰掰！

📢 雲羽生存服 管理團隊 - <@{self.starter}> 敬上
<t:{self.timestamp}:F>

[ ||<@&1190290928112517212>||  |  ||<@&1190291336750960773>||  |  ||<@&1190298140692185128>||  |  ||<@&1186541054514704434>||]
"""

class FixMsgGen():
    def __init__(
        self,
        intro: str = """
抱歉各位，我們發現了一些問題，已經排定將要開始修復...
我們很快就會開始處理，希望大家給我們一些時間 >_<
為了提供更棒的遊戲環境，希望大家見諒！
""",
        content: list = [
            "修復一些錯誤"
        ],
        reason: str = "未知原因",
        time: dict = {
            "begin": "還未排定",
            "end": "還未排定"
        },
        starter: str = "959977374471028779"
    ):
        self.intro = intro
        # 將content轉換成字串，並在字串前方加上減號與空格使其可以直接放入markdown中
        self.content = "\n".join([f"- {i}" for i in content])
        # 利用datetime將當前時間轉換成UNIX時間戳（字串）
        self.timestamp = str(datetime.datetime.now().timestamp())
        self.reason = reason
        self.start = time["begin"]
        self.end = time["end"]
        self.starter = starter
#         self.text = f"""
# ## 雲羽維修

# {self.intro}

# ### 維修原因
# {self.reason}

# ### 維修預計時間
# - **<a:928961403749019649:1198243923915718706> 開始**：{self.start}
# - **<a:928961427685904385:1198243930731458651> 結束**：{self.end}

# ### 維修造成影響
# {self.content}

# ### 維修狀態
# <:dangerous:1254019093900558397> 還未開始


# 很抱歉打擾各位的生活了，希望各位見諒
# 為了維持完美的遊戲體驗，讓我們一起共創更美好的伺服器！<a:yeees:1197923046149853195> 

# 📢 雲羽生存服 管理團隊 - <@{self.starter}> 敬上

# [ ||<@&1190290928112517212>||  |  ||<@&1190291336750960773>||  |  ||<@&1190298140692185128>||  |  ||<@&1186541054514704434>||]
# """
        try:
            self.text = cfg["fix_format"].format(
                intro=self.intro,
                reason=self.reason,
                start=self.start,
                end=self.end,
                content=self.content,
                starter=self.starter
            )
        # 在格式化中找不到佔位符時會報錯，這時就回報錯誤
        except KeyError:
            logger.warning("找不到佔位符，將使用預設訊息")
            self.text = f"""
## 伺服器維修

{self.intro}

### 維修原因
{self.reason}

### 維修預計時間
- **<a:928961403749019649:1198243923915718706> 開始**：{self.start}
- **<a:928961427685904385:1198243930731458651> 結束**：{self.end}

### 維修造成影響
{self.content}

### 維修狀態
<:dangerous:1254019093900558397> 還未開始


很抱歉打擾各位的生活了，希望各位見諒
為了維持完美的遊戲體驗，讓我們一起共創更美好的伺服器！<a:yeees:1197923046149853195> 

📢 雲羽生存服 管理團隊 - <@{self.starter}> 敬上

[ ||<@&1190290928112517212>||  |  ||<@&1190291336750960773>||  |  ||<@&1190298140692185128>||  |  ||<@&1186541054514704434>||]
"""