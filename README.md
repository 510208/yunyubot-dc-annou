![image](https://github.com/510208/yunyubot-dc-annou/assets/107909497/b0a0cc43-1769-4ef7-b17f-704851b0175e)


# CloudFeather Announcement Bot

這是一個提供給 [🪶Minecraft 雲羽伺服器](https://discord.gg/CfGvx3NQWZ) 的 Discord Bot，由服主 SamHacker 編寫。為了幫助更多人而不限於我們伺服器內部，我將此專案開源出來給大家使用

## 💻 如何部署？

你可以使用虛擬環境或直接搭建，以下分析兩種方式的優缺點：

| | [**📦 虛擬環境**](#-虛擬環境) | [**⏰ 直接搭建**](#-直接搭建) |
|:---|:---|:---|
| **原理** | 在電腦上建立一個虛擬的、與本機隔離的獨立 Python 環境，<br>並在那之中運行機器人，就像沙箱一樣！ | 使用原本就安裝在電腦上的 Python 原生環境直接運行機器人，<br>這種方法你可以打少少的指令完成一個部署，期待嗎？
| **優點** | <li>無須擔心為了機器人妨礙到其他 Python 軟體的執行<li>可提供更佳的彈性 | <li>部署較為簡單<li>耗用儲存空間較少 |
| **缺點** | <li>部署較為麻煩<li>每次執行前需要先切換進虛擬環境中 | <li>容易造成環境衝突<li>後期糾錯較為麻煩 |

### 📦 虛擬環境

搭建在 Python 虛擬環境中是個不錯的主意！如此一來，你可以比較不需要擔心插件衝突的問題，並且它提供了你未來擴充機器人的彈性。想像一下，未來你的機器人可以幫你管整個 Minecraft 伺服器，聽起來是不是很心動？

心動不如馬上行動，我們開始吧！

1. 先前往 [Python官網](https://www.python.org/) 下載並安裝 Python
> 喔對了！我使用的是 Python 3.10.6，我可以保證這個版本下的程式可以正常運作！
> 
> 請記得，安裝時必須要勾選 `Add Python 3.x to PATH`，否則待會的操作會很麻煩喔...
2. 安裝完成後，你可以在網頁最上面有綠色`<> Code`按紐，按下它之後點選"Download ZIP"（在最下方），下載後解壓縮
   （Zip格式可以用Windows 10以上的系統解壓）
3. 按住Shift鍵並在資料夾中右鍵，選擇"使用PowerShell開啟"
4. 會跳出一個看起來很複雜的視窗，不用怕，直接貼上下面這段就好，記得一行一行貼：
```shell
$ python -m venv
$ cd .venv/Scripts
$ activate
$ pip install -r requirements.txt
```
> 請記得，前面的錢號不用打進去，那代表你要自己輸入的意思
5. 現在你搭建好了！恭喜你！！

### ⏰ 直接搭建

很簡單，首先先照上方虛擬方式的方法執行，但你只需要打這些指令即可：

```shell
$ pip install -r requirements.txt
```
（是的沒錯就這麼少）

### 🔒 建立機器人

如果你看到了這裡，恭喜你已經完成了一半！再來你需要去建立一個 Discord 機器人，請照以下教學處理：

1. 前往 [https://discord.com/developers/applications](https://discord.com/developers/applications) 網站並登入自己的 Discord 帳號
2. 單按右上紫色的 "New Applaction"，它會幫你建立一個新的機器人。然後會跳出一個如圖的訊息，輸入你希望機器人的名字，然後打勾勾按 Create 建立機器人：

![image](https://github.com/510208/yunyubot-dc-annou/assets/107909497/f5363ebd-c448-4ca8-a0e6-9ef448949aab)

3. 切換到左列的 Bot，將底下三個 "Privileged Gateway Intents" 的勾都勾上：

![image](https://github.com/510208/yunyubot-dc-annou/assets/107909497/44ceb53d-4776-404c-b6b6-e2a6900fa8b3)

4. 滑到上方，單按 Token 下大大的 "Reset Token"。點下去，如果你有雙步驟驗證請打一下驗證碼：

![image](https://github.com/510208/yunyubot-dc-annou/assets/107909497/27994e32-8374-457f-8ebe-023263df4489)

5. 看到一組亂碼，存下來千萬別告訴別人。打開軟體的資料夾找到 `token.txt`（沒有的話自己創建也可以），將剛剛的亂碼貼進這個文件中

> 這組亂碼跟你的密碼是一樣的，因此千萬要小心不要分享給人。只要別人擁有這組亂碼，他就可以在你的 Discord 群組中為所欲為！

### ▶ 機器人，啟動！！

恭喜你進度條到了99%，剩下最後一件事就是雙按 `main.py` 啟動機器人。

如果看到類似以下的訊息，代表你已經可以去找機器人...了嗎？
```log
228: [2024-06-29 21:16:46,384][INFO] - [main] 載入annou_stat.py中...
30: [2024-06-29 21:16:46,412][INFO] - [annou_stat] AnnouStat cog 已經載入
230: [2024-06-29 21:16:46,415][INFO] - [main] 載入annou_stat.py成功
237: [2024-06-29 21:16:46,416][INFO] - [main] 跳過nlfile.py, 原因：採用nl方式跳過載入
239: [2024-06-29 21:16:46,416][INFO] - [main] 跳過__pycache__
603: [2024-06-29 21:16:46,417][INFO] - [client] logging in using static token
561: [2024-06-29 21:16:48,248][INFO] - [gateway] Shard ID None has connected to Gateway (Session ID: 6989b35e31230ee56a079ae50220d5a3).
28: [2024-06-29 21:16:50,347][INFO] - [main] Logged in as (機器人名稱)#(機器人編號) (ID: 機器人ID)
```

### 🤝 邀請機器人

對，現在機器人啟動了。但你有沒有發現一件事情：

> 我的伺服器裡還是沒這隻機器人啊！！！！

因此讓我們邀請機器人吧！

1. 切換到 [https://discord.com/developers/applications](https://discord.com/developers/applications)，點擊你剛剛建立好的機器人之後切換到左列 OAuth 中：

![image](https://github.com/510208/yunyubot-dc-annou/assets/107909497/a3acf2ee-2295-4a9a-b495-be47ff2cc9c9)

2. 拉到下方 `OAuth2 URL Generator`，勾選bot，然後勾選"Adminstrator"給機器人管理權限
3. `GENERATED URL`即為邀機器人進服的方法！

## ⛏ 編輯配置

> [!CAUTION]
> 編輯完配置後記得要關閉機器人並重新開啟以加載新版本

先跟各位使用者說聲抱歉，我沒有辦法編寫配置文件。如果有人願意協助我編寫，我會很感激的！

### 公告引言

`nltemplate.py`文件裡頭存放了預設的公告文字格式，你可以對它進行修改

在最開始的代碼中，你會看到這幾行字：
```python
        intro: str = """
太棒了！我們伺服器又更新了~~
快來看看這次我們又更新了些啥吧，快點喔！
""",
```
你可以把三個引號包起來的內容改成你想要的任何文句，這是預設的公告引言~~

如果你在下方又看到類似的intro，不用訝異不用驚喜，這是維修公告的預設引言：
```python
        intro: str = """
抱歉各位，我們發現了一些問題，已經排定將要開始修復...
我們很快就會開始處理，希望大家給我們一些時間 >_<
為了提供更棒的遊戲環境，希望大家見諒！
""",
```

### 公告格式
它應該在`nltemplate.py`的第44行左右，那段文字是預設的公告格式，看起來像這樣：

![image](https://github.com/510208/yunyubot-dc-annou/assets/107909497/4908f143-687b-4b75-8a70-40614cb11f54)

是的你想的沒錯，在68行處有一個是用來作維修公告的版型，一樣可以改：

![image](https://github.com/510208/yunyubot-dc-annou/assets/107909497/4788b679-254e-4fd1-b1a3-0360221b8c87)

以下是你可以用的一些佔位符，發布公告時這些地方會被換成正確的東西：

- `{self.intro}`：公告引言，表單中填寫
- `{self.content}`：更新內容（或維修造成影響）
- `{self.starter}`：發公告的人，會用@的
- `{self.timestamp}`：發公告時的 Unix 時間戳，它通常應該這樣用：`<t:{self.timestamp}:F>`
- `{self.reason}`：維修原因，只有在維修公告處有用，放在更新公告會報錯！
- `{self.start}`、`{self.end}`：維修開始與結束時間

你可以任意填寫以上提供的選項在你的模板中，但請記得不要移除前後的大括號，否則版型仍然會出錯喔！

### 停用部分模組

以下表格是目前有的模組列表，位於`Cogs`資料夾中：

| **檔案名稱** | **用途** | **開發者** | **備註** |
|:--- |:---|:---|:---|
| `annou.py` | 發送公告的程式碼，內建有兩種公告型式 | @510208 |  |
| `annou_stat.py` | 修改維修公告狀態的程式碼 | @510208 | |
| `about.py` | 關於機器人 | @510208 | |

未經提及的檔案與`nl`開頭的檔案請直接視為測試檔案，它們並不重要

如果要停用某個模組或它不應該被視為模組載入（它可能是某個模組需要的函式庫、程式碼等，但它的結尾為.py檔案時），請為該檔案檔名最前方加上`nl_`（只需要nl開頭即可，加上底線是為了未來識別方便）即可。例如試圖停用`about.py`，你可以將它改名為`nl_about.py`（或任何以nl開頭的檔名，nl代表Not Load）。主模組會自動載入的檔案須滿足以下條件：

1. 檔名不由nl開頭
2. 是Python原始碼格式（也就是副檔名.py）

倘若檔案違反以上任何規則，程式就會在終端機透過訊息提示不載入與其原因

### 更改關於頁面的作者訊息

> [!IMPORTANT]
> 請在 about 提供的資訊中保留原作者的資訊，謝謝您的使用！

如果你要更改關於頁面的作者訊息，請照以下說明：

1. 進入`/Cogs/about.py`
2. 定位到`async def about(self, interaction: discord.Interaction):`的位置，下方就是關於頁面訊息內容
3. 以下是詳細說明：

#### 標題與簡述

```python
embed = discord.Embed(
    title = "關於",
    description = "這是雲羽生存服專用的機器人\n由插件師兼伺服器工程師SamHacker搭建",
    color = 0x00ff00
)
```

- `title`：標題，建議保持預設
- `description`：說明，請記得文句要用`\n`斷行，以及不能手動換行
- `color`：Embed的顏色

#### 作者名與相同格式內容

```python
embed.add_field(
    name = "作者",
    value = "SamHacker"
)
```

- `value`：內容，請照情況修改

> [!IMPORTANT]
> 作者欄請記得要保留我的名稱，謝謝

#### 大頭貼

```python
# 設定大頭貼
embed.set_thumbnail(url="https://gravatar.com/avatar/f7598bd8d4aba38d7219341f81a162fc842376b3b556b1995cbb97271d9e2915?s=256")
```

將`url`後方的字串修改即可

其他部分請照說明的方式修改，也可不修改

## 🆖 協助開發

首先，我個人也不是什麼太厲害的人，對於這邊的貢獻流程如果有建議歡迎提Issue補充！總之非常感謝你願意看到這一步，如果你也想為這個專案做貢獻，請照以下說明操作：

### ❗ 常見錯誤

#### 特權網關意圖錯誤

```
discord.errors.PrivilegedIntentsRequired: Shard ID None is requesting privileged intents that have not been explicitly enabled in the developer portal. It is recommended to go to https://discord.com/developers/applications/ and explicitly enable the privileged intents within your application's page. If this is not possible, then consider disabling the privileged intents instead.
```

以上是特權網關意圖錯誤，如果你的錯誤碼類似這樣，請前往 [Discord Developer Portal](https://discord.com/developers/applications)，進入機器人選項後在Bots底下的"Privileged Gateway Intents"全部勾選後Save並且重啟即可排除

#### Token錯誤

```
discord.errors.LoginFailure: Improper token has been passed.
```

類似以上訊息，可能是你的 Token 錯誤。請照上方教學重新前往開發者面板並取得新的 Token 後 再次嘗試，仍然錯誤再前來詢問


> [!CAUTION]
> 如果 Token 被你誤發到 Github 等平台，Discord 也會自動重置該組 Token 以防止意外發生

### ❓ 遇到問題

如果你遇到以下情況，請照這個章節的說明操作：

- 遇到Traceback錯誤以致無法執行或啟動
- 執行或啟動過程中遇到Traceback錯誤，但仍能繼續走流程
- 或其他問題適合提Issue

請在 [Issues](https://github.com/510208/yunyubot-dc-annou/issues) 中提出問題，並提供以下必須資訊（如果不提供或找不到，我們有權利不做受理）：

- Python版本與機器人版本（可以透過Git檢視Commit的編號）
- 錯誤內容
- 如何啟動這個錯誤
- 發現時間
- 是否已經確定不是自己問題

有部分錯誤已知解決方法並列在常見錯誤區段中，請自行先做檢查後再提 Issue，否則我們有權不受理

### ❤ 協助開發

非常謝謝你願意協助這個機器人的完善，未來我會考慮更換一下這個機器人的名稱。順帶一提，本機器人應該不會是 [Nether Bot](https://github.com/510208/nether) 的繼承人（至少現在不會）

如果你要協助開發，請參考[CONTRIBUTING.md](CONTRIBUTING.md)的描述，謝謝您

### 💗 贊助專案

> [!IMPORTANT]
> 我們目前不接受任何格式的贊助，非常遺憾

## 🙏 備註與謝誌

非常感謝 @510208 的開發，與以下用戶的協助：

| **用戶或團體** | **內容** |
|:---|:---|
| [雲羽生存服](https://discord.gg/CfGvx3NQWZ) | 提供Discord群組做為測試之用 |
| [Asteroid Bot Hosting](https://discord.gg/DuJEFKqckm) | 提供機器人24小時託管 |
| LunarKdeo3147 | 協助測試專案與提供建議 |

與你的使用！
