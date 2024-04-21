import telebot
import sqlite3

TOKEN = "6817294069:AAF3j9_KFBpAebKzmA22dvjxVZ3yoX0PWvk"
adminUserID = 5752084510

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

# Add user to Braodcast list on /start.
@bot.message_handler(commands=['start'])
def addUsertoBroadcast(message):

    userId = message.from_user.id
    firstName = message.from_user.first_name
    userName = message.from_user.username

    bot.reply_to(message, f"Hello {firstName}👋!\nWelcome to the bot!")


    con = sqlite3.connect("users.db")
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS user(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL, 
                    first_name TEXT NOT NULL,
                    username TEXT,
                    UNIQUE(user_id) 
            ); ''')

    try:
        cur.execute(f"""
        INSERT INTO user(user_id, first_name, username) 
        VALUES({userId}, "{firstName}", "{userName}")
        """)

        print(f"👤 New User: {firstName}")

    except sqlite3.IntegrityError:
        print(f"{firstName} is already exist on your database.")
        
    con.commit()
    con.close()



# Send /broadcast message
@bot.message_handler(commands=['broadcast'])
def broadcast_message(message):


    # Check the permissions
    if message.from_user.id != adminUserID:
        bot.reply_to(message, "❌ Only admins allowed to use this command.")
        return

    # Send the broadcast message to all users
    if message.reply_to_message:
        replyMessageID = message.reply_to_message.message_id

        con = sqlite3.connect("users.db")
        cur = con.cursor()

        userList = cur.execute("SELECT * FROM user")
        
        print("Starting a New Broadcast.. 📡\n-------------------------------")
        for userChatID in userList:
            print(f"{userChatID[1]} : {userChatID[2]} Sent. ✅")

            # With Forwarded Tag
            # bot.forward_message(userChatID[1], message.chat.id, replyMessageID)

            # Without Forwarded Tag
            bot.copy_message(chat_id=userChatID[1], from_chat_id=message.chat.id, message_id=replyMessageID)

        con.commit()
        con.close()


    else:
        bot.reply_to(message, "Please reply to the message you want to broadcast.")


# Start the bot
print("Broadcast bot is running..")
bot.infinity_polling()
