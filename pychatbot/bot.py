import telebot
from synthesis import run_synthesis
from decouple import config
bot = telebot.TeleBot(config('TOKEN_ID'))

def extract_message_arg(arg):
    content_message = arg.split()[1:]
    return ' '.join(content_message)

@bot.message_handler(commands=['say'])
def echo_all(message):
    text = extract_message_arg(message.text)
    chat_id = message.chat.id
    print(text)
    voice = run_synthesis(text, lang='pt-BR')
    bot.send_voice(chat_id, voice)

@bot.message_handler(content_types=['new_chat_members'])
def welcome_message(message):
    name = message.new_chat_members[0].first_name
    wc_msg = f"Welcome {name} to our group and fuck off"
    voice = run_synthesis(wc_msg)
    bot.send_voice(message.chat.id, voice)

bot.polling()

#regexp='((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)'