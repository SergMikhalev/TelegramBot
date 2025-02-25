import telebot
from config import keys,TOKEN
from extensions import CryproConverter,ConvertionExeption

bot = telebot.TeleBot(TOKEN)
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
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise ConvertionExeption('Слишком много параметров')
        quot, base, ammount = values
        total_base = CryproConverter.convert(quot,base,ammount)
    except ConvertionExeption as e:
        bot.reply_to(message, f'Ошибка пользователя\n {e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена за {ammount}  {quot} в {base} - {total_base} '
        bot.send_message(message.chat.id, text)

bot.polling()
