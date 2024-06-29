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

5. 看到一組亂碼，存下來千萬別告訴別人。打開軟體的資料夾找到 `token.txt` ，將剛剛的亂碼貼進這個文件中
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

> **請注意！！**
>
> 編輯完後記得要關閉機器人並重新開啟喔！

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

