import telebot
from synthesis import run_synthesis
from decouple import config
bot = telebot.TeleBot(config('TOKEN_ID'))


@bot.message_handler(func=lambda m: True
    #regexp='((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)'
    )
def echo_all(message):
    print(message.text)
    voice = run_synthesis(message.text)
    bot.send_voice(config('CHAT_ID'), voice)

bot.polling()