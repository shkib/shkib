import telebot;

from telebot import types
bot = telebot.TeleBot('1026954843:AAHIe857Stm4VsCpFlG6tH1QQht4A724lPM');

markup_menu = types.ReplyKeyboardMarkup ( resize_keyboard=True, row_width=1)
btn_adress = types.KeyboardButton ('АДреса магазинов', request_location=True)
btn_payment = types.KeyboardButton ( 'Способы оплаты')
btn_delivery = types.KeyboardButton ( 'Способы доставки')
markup_menu.add(btn_adress, btn_delivery, btn_payment)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Здарова! Хочу показать чему научился! Начнем?", reply_markup =markup_menu)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "Способы доставки":
        bot.reply_to(message, "Доставка курьером, самовывоз, ПОчта Росии", reply_markup= markup_menu)
    elif message.text == "Способы оплаты":
        bot.reply_to(message, "Наличные, Картой", reply_markup= markup_menu)
    else:
        bot.reply_to(message, message.text, reply_markup= markup_menu)


@bot.message_handler(func=lambda message: True, content_types=['location'])
def magazin_location(message):
    lon = message.location.longitude
    lat = message.location.latitude
    print('Широта {} Долгота {}'.format(lon, lat))
bot.polling()
