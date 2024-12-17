# <p align="center">Telegram Broadcast Bot 📢</p>
<p align="center">A Telegram bot to send broadcast messages to all the users on the bot.</p>
<p align="center"><i>(Only for Educational Purposes)</i></p>

#
## 🔧 Features 
- ✅ Ease of use.
- ✅ Including text, images and markdown are supported.
- ✅ Show/Hide Forwarded tag.
- ✅ Unlimited Users.
- ✅ User Database with SQLite3.
- ✅ NO PAID PLANS.
- ✅ No Developer side limits.
- ✅ Beginner friendly code.
- ✅ Extensible with any [pytelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI/) bot.

## 👥 Usage
### How to register users?
- Upon receiving this /start from the users, their information will be automatically added to a SQLite database.
- Users `user_id`, `first_name`, `username` will be collected.
- Fork the repo and modify the code, if you want more features.

### Send Broadcast messages
- Simply send a reply to your broadcast message as /broadcast. Replied message will sent to to all the users in the bot (from the database).

## ♻ How to Deploy
### Requirements
- Python 3.x.x
- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI/) library.

### Setup local variables
- Get your _BOT_API_KEY_ from [here](https://core.telegram.org/bots/tutorial#obtain-your-bot-token).
- Replace your api key with `TOKEN` variable in [bot.py](https://github.com/hansanaD/Telegram-Broadcast-Bot/blob/master/bot.py).
- Example: ```TOKEN = "09876543210:AAHePL8-xSzjOlnF5dRGiwhNyxxZsS3u7f4"```
- Get your _UserID_ from [here](https://t.me/userinfobot).
- Replace your user id with `adminUserID` variable in [bot.py](https://github.com/hansanaD/Telegram-Broadcast-Bot/blob/master/bot.py).
- Example: ```adminUserID = 1234567890"```
- Save!
  
#
### Install & Run
```
git clone https://github.com/hansanaD/Telegram-Broadcast-Bot.git;
cd Telegram-Broadcast-Bot;
pip install -r requirements.txt;
python bot.py
```
#

## ‼ Disclaimer
This repository is intended for educational and personal use only. The use of this repository for any commercial or illegal purposes is strictly prohibited. **Spamming or misuse of the broadcast feature is strictly prohibited.** Users are expected to adhere to Telegram's terms of service. The repository owner is not responsible for any misuse of the software or any legal consequences that may arise from such misuse

- **APIs : [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI/)**
- **Contact for issues : [@dev00111](https://t.me/dev00111_bot)**


