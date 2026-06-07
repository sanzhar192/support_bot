import telebot
from config import token
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, я бот!")
@bot.message_handler(func=lambda message: message.text=="Привет")
def send_image(message):
    with open("image.jpg", "rb") as image:
        bot.send_photo(message.chat.id, image)
bot.polling()