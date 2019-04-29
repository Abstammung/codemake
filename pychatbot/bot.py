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
    wc_msg = f"Olá {name}, seja bem-vindo ao nosso grupo foda."
    voice = run_synthesis(wc_msg, lang="pt-BR")
    bot.send_voice(message.chat.id, voice)

@bot.message_handler(commands=['bitcoin'])
def get_dolar(message):
    import json
    import requests
    response = requests.get('https://www.mercadobitcoin.net/api/BTC/ticker/')
    data = json.loads(response.content)["ticker"]
    sell, buy = float(data["sell"]), float(data["buy"])
    cotacao = 'Bitcoin - Mercado Bitcoin\nVenda: {0:.2f}\nCompra: {1:.2f}'.format(sell, buy)
    bot.send_message(message.chat.id, cotacao)

bot.polling()

#regexp='((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)'