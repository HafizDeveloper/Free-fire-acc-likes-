import telebot
import requests

# Replace with your Telegram bot token
BOT_TOKEN = "7613718217:AAF0-eF30Coi4cl_U4fhsYvI7s7ezMZ29ks"

# Initialize the bot
bot = telebot.TeleBot(BOT_TOKEN)

# Function to send likes using Free Fire API
def send_likes(uid):
    url = "https://ff-community-api.vercel.app/sendLikes"
    params = {
        "uid": uid,
        "access_key": "55sub"
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return f"✅ Success: {response.json()}"
    else:
        return f"❌ Error {response.status_code}: {response.text}"

# Command to start the bot
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Send a Free Fire UID to send likes.\nExample: `12345678`", parse_mode="Markdown")

# Handling user messages (UID input)
@bot.message_handler(func=lambda message: message.text.isdigit())
def handle_uid(message):
    uid = message.text
    response = send_likes(uid)
    bot.reply_to(message, response)

# Run the bot
bot.infinity_polling()