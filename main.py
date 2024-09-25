import telebot
from telebot import types
from Token import Token
import os
from gtts import gTTS

bot = telebot.TeleBot(Token)

#Старт
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add(types.KeyboardButton('Зал №1'))
    keyboard.add(types.KeyboardButton('Зал №2'))
    bot.send_message(message.chat.id, 'Введите номер экспонат, которй вас интерисует', reply_markup=keyboard)

#Помощь
@bot.message_handler(content_types=['text'])
def main(message):
    if message.text == 'Помощь':
        bot.send_message(message.chat.id, 'Добрый день. Я помощница под именем Лулу. '
                         'Если вас что-то интереует, то просто подойдите к работнику музея и сросите, что вас интерсует')

#Зал №1
@bot.message_handler(content_types=['text'])
def Hall_No_1(message):
    if message.text == 'Зал №1':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton('Экспонат №1', callback_data='Esponyat No.1'))
        keyboard.add(types.InlineKeyboardButton('Экспонат №2', callback_data='Esponyat No.2'))
        keyboard.add(types.InlineKeyboardButton('Экспонат №3', callback_data='Esponyat No.3'))
        keyboard.add(types.InlineKeyboardButton('Экспонат №4', callback_data='Esponyat No.4'))
        bot.send_message(message.chat.id, 'Выберите номер экспоната, которй вас интересует в "Зал №1"', reply_markup=keyboard)

#Зал №2
@bot.message_handler(content_types=['text'])
def Hall_No_2(message):
    if message.text == 'Зал №2':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton('Экспонат №1', callback_data='Esponyat No.1.2'))
        keyboard.add(types.InlineKeyboardButton('Экспонат №2', callback_data='Esponyat No.2.2'))
        keyboard.add(types.InlineKeyboardButton('Экспонат №3', callback_data='Esponyat No.3.2'))
        keyboard.add(types.InlineKeyboardButton('Экспонат №4', callback_data='Esponyat No.4.2'))
        bot.send_message(message.chat.id, 'Выберите номер экспоната, которй вас интересует в "Зал №2"', reply_markup=keyboard)

#Экспонаты
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'Esponyat No.1':
        tts=gTTS("Экспонат №1, Зал №1. Картина Пётра I Алексе́евича, Пётр Вели́кий родился 30 мая 1672, Москва, умер 28 января 1725, в Санкт-Петербурге — царь всея Руси с 1682 года, первый император Всероссийский с 1721 года.", lang="ru", slow=False)
        tts.save(f"{call.from_user.id}.mp3")
        file = open(f"{call.from_user.id}.mp3", 'rb')
        bot.send_voice(call.message.chat.id, file, caption="Экспонат №1, Зал №1. Картина Пётра Первого Алексе́евича, Пётр Вели́кий родился 30 мая 1672, Москва, умер 28 января 1725, в"
             "Санкт-Петербурге — царь всея Руси с 1682 года, первый император Всероссийский с 1721 года.")
        os.remove(f"{call.from_user.id}.mp3")

    elif call.data == 'Esponyat No.2':
        tts=gTTS('"Экспонат №2, Зал №1. Иван Четвёртый Васильевич родился 1530 умер 1584 — государь, царь и великий князь всея Руси с 1533 года, первый венчанный царь всея Руси с 1547 года.',lang="ru",slow=False)
        tts.save(f"{call.from_user.id}.mp3")
        file = open(f"{call.from_user.id}.mp3", 'rb')
        bot.send_voice(call.message.chat.id, file, caption='Экспонат №2, Зал №1. Иван IV Васильевич (1530–1584) — государь, царь и великий князь всея Руси с 1533 года, первый венчанный царь всея Руси (с 1547 года).')
        os.remove(f"{call.from_user.id}.mp3")

    elif call.data == 'Esponyat No.3':
        tts=gTTS("Экспонат №3, Зал №1. Подарок турецкого султана Абдул-Хамида Первого, императрице Екатерине II в 1775 году. Представляет собой украшение" 
             "для лошади инкрустирована дорогим сапфиром и покрыт серебром.",lang="ru",slow=False)
        tts.save(f"{call.from_user.id}.mp3")
        file = open(f"{call.from_user.id}.mp3", 'rb')
        bot.send_voice(call.message.chat.id, file,caption="Экспонат №3, Зал №1. Экспонат №3. Подарок турецкого султана Абдул-Хамида Первого, императрице Екатерине II в 1775 году. Представляет собой украшение" 
             "для лошади инкрустирована дорогим сапфиром и покрыт серебром.")
        os.remove(f"{call.from_user.id}.mp3")

    elif call.data == 'Esponyat No.4':
        tts=gTTS('Экспонат №4, Зал №1. Учебник который был написан великил учёным нашего времени.',lang="ru",slow=False)
        tts.save(f"{call.from_user.id}.mp3")
        file = open(f"{call.from_user.id}.mp3", 'rb')
        bot.send_voice(call.message.chat.id, file,caption='Экспонат №4, Зал №1. Учебник который был написан великим учённым нашего времени.')
        os.remove(f"{call.from_user.id}.mp3")

    elif call.data == 'Esponyat No.1.2':
        tts=gTTS('"Экспонат №1, Зал №2. Иван Четвёртый Васильевич родился 1530 умер 1584 — государь, царь и великий князь всея Руси с 1533 года, первый венчанный царь всея Руси с 1547 года.',lang="ru",slow=False)
        tts.save(f"{call.from_user.id}.mp3")
        file = open(f"{call.from_user.id}.mp3", 'rb')
        bot.send_voice(call.message.chat.id, file, caption='Экспонат №1, Зал №2. Иван IV Васильевич (1530–1584) — государь, царь и великий князь всея Руси с 1533 года, первый венчанный царь всея Руси (с 1547 года).')
        os.remove(f"{call.from_user.id}.mp3")

    elif call.data == 'Esponyat No.2.2':
        tts=gTTS('"Экспонат №2, Зал №2. Иван Четвёртый Васильевич родился 1530 умер 1584 — государь, царь и великий князь всея Руси с 1533 года, первый венчанный царь всея Руси с 1547 года.',lang="ru",slow=False)
        tts.save(f"{call.from_user.id}.mp3")
        file = open(f"{call.from_user.id}.mp3", 'rb')
        bot.send_voice(call.message.chat.id, file, caption='Экспонат №2, Зал №2. Иван IV Васильевич (1530–1584) — государь, царь и великий князь всея Руси с 1533 года, первый венчанный царь всея Руси (с 1547 года).')
        os.remove(f"{call.from_user.id}.mp3")

    elif call.data == 'Esponyat No.3.2':
        tts=gTTS('"Экспонат №3, Зал №2. Иван Четвёртый Васильевич родился 1530 умер 1584 — государь, царь и великий князь всея Руси с 1533 года, первый венчанный царь всея Руси с 1547 года.',lang="ru",slow=False)
        tts.save(f"{call.from_user.id}.mp3")
        file = open(f"{call.from_user.id}.mp3", 'rb')
        bot.send_voice(call.message.chat.id, file, caption='Экспонат №3, Зал №2. Иван IV Васильевич (1530–1584) — государь, царь и великий князь всея Руси с 1533 года, первый венчанный царь всея Руси (с 1547 года).')
        os.remove(f"{call.from_user.id}.mp3")

    elif call.data == 'Esponyat No.4.2':
        tts=gTTS('"Экспонат №4, Зал №2. Иван Четвёртый Васильевич родился 1530 умер 1584 — государь, царь и великий князь всея Руси с 1533 года, первый венчанный царь всея Руси с 1547 года.',lang="ru",slow=False)
        tts.save(f"{call.from_user.id}.mp3")
        file = open(f"{call.from_user.id}.mp3", 'rb')
        bot.send_voice(call.message.chat.id, file, caption='Экспонат №4, Зал №2. Иван IV Васильевич (1530–1584) — государь, царь и великий князь всея Руси с 1533 года, первый венчанный царь всея Руси (с 1547 года).')
        os.remove(f"{call.from_user.id}.mp3")

bot.stop_polling()
bot.polling(none_stop=True)