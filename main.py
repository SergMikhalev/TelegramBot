from multiprocessing.managers import Token
from shlex import quote
from turtledemo.penrose import start
import json

import requests
import telebot
from urllib3 import request

TOKEN = '7812640556:AAEaoaKh2PzpvjMCv6VHhh3ttmGBIovNwtU'
bot = telebot.TeleBot(TOKEN)
keys = {
    'Рубль': 'RUB',
    'Доллар': 'USD',
    'Евро': 'EUR',
}
@bot.message_handler(commands = ['start','stop'])
def help(message: telebot.types.Message):
    text = 'Для начала работы введите команду в следующем формате: \n\
    <имя валюты>\n\
    <в какуб валюту перевести>\n\
    <количество переводимой валюты>\n Доступные валюты /values'
    bot.reply_to(message, text)

@bot.message_handler(commands= ['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты: '

    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message,text)

@bot.message_handler(content_types='text')
def convert(message:telebot.types.Message):
    quot,base,ammount = message.text.split(' ')
    r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms={keys[quot]},{keys[base]}')
    total_base = json.loads(r.content)[keys[base]]
    text = f'Цена за {ammount}  {base} в {quot} - {total_base} '
    bot.send_message(message.chat.id, text)







bot.polling()
