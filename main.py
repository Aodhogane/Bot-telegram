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

#Зал №1
@bot.message_handler(content_types=['text'])
def Hall_No_1(message):
    if message.text == 'Зал №1':
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add(types.KeyboardButton('Экспонат №1'))
        keyboard.add(types.KeyboardButton('Экспонат №2'))
        keyboard.add(types.KeyboardButton('Экспонат №3'))
        keyboard.add(types.KeyboardButton('Экспонат №4'))
        bot.send_message(message.chat.id, 'Выберите номер экспоната, которй вас интересует в "Зал №1"', reply_markup=keyboard)

    elif message.text == 'Экспонат №1':
        tts=gTTS("Экспонат №1, Зал №1. Картина Пётра I Алексе́евича, Пётр Вели́кий родился 30 мая 1672, Москва, умер 28 января 1725, в Санкт-Петербурге — царь всея Руси с 1682 года, первый император Всероссийский с 1721 года.", lang="ru", slow=False)
        tts.save(f"{message.from_user.id}.mp3")
        file = open(f"{message.from_user.id}.mp3", 'rb')
        try:
            bot.send_voice(message.chat.id, file, caption="Экспонат №1, Зал №1. Картина Пётра Первого Алексе́евича, Пётр Вели́кий родился 30 мая 1672, Москва, умер 28 января 1725, в"
             "Санкт-Петербурге — царь всея Руси с 1682 года, первый император Всероссийский с 1721 года.")
        finally:
            file.close()
        os.remove(f"{message.from_user.id}.mp3")

    elif message.text == 'Экспонат №2':
        tts=gTTS('"Экспонат №2, Зал №1. Иван Четвёртый Васильевич родился 1530 умер 1584 — государь, царь и великий князь всея Руси с 1533 года, первый венчанный царь всея Руси с 1547 года.',lang="ru",slow=False)
        tts.save(f"{message.from_user.id}.mp3")
        file = open(f"{message.from_user.id}.mp3", 'rb')
        try:
            bot.send_voice(message.chat.id, file, caption='Экспонат №2, Зал №1. Иван IV Васильевич (1530–1584) — государь, царь и великий князь всея Руси с 1533 года, первый венчанный царь всея Руси (с 1547 года).')
        finally:
            file.close()
        os.remove(f"{message.from_user.id}.mp3")

    elif message.text == 'Экспонат №3':
        tts=gTTS("Экспонат №3, Зал №1. Подарок турецкого султана Абдул-Хамида Первого, императрице Екатерине II в 1775 году. Представляет собой украшение" 
             "для лошади инкрустирована дорогим сапфиром и покрыт серебром.",lang="ru",slow=False)
        tts.save(f"{message.from_user.id}.mp3")
        file = open(f"{message.from_user.id}.mp3", 'rb')
        try:
            bot.send_voice(message.chat.id, file,caption="Экспонат №3, Зал №1. Экспонат №3. Подарок турецкого султана Абдул-Хамида Первого, императрице Екатерине II в 1775 году. Представляет собой украшение" 
             "для лошади инкрустирована дорогим сапфиром и покрыт серебром.")
        finally:
            file.close()
        os.remove(f"{message.from_user.id}.mp3")

    elif message.text == 'Экспонат №4':
        tts=gTTS('Экспонат №4, Зал №1. Учебник который был написан великил учёным нашего времени.',lang="ru",slow=False)
        tts.save(f"{message.from_user.id}.mp3")
        file = open(f"{message.from_user.id}.mp3", 'rb')
        try:
            bot.send_voice(message.chat.id, file,caption='Экспонат №4, Зал №1. Учебник который был написан великим учённым нашего времени.')
        finally:
            file.close()
        os.remove(f"{message.from_user.id}.mp3")  

    if message.text == 'Зал №2':
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add(types.KeyboardButton('Экспонат №1'))
        keyboard.add(types.KeyboardButton('Экспонат №2'))
        keyboard.add(types.KeyboardButton('Экспонат №3'))
        keyboard.add(types.KeyboardButton('Экспонат №4'))
        bot.send_message(message.chat.id, 'Выберите номер экспоната, которй вас интересует в "Зал №2"', reply_markup=keyboard)

    elif message.text == 'Экспонат №1':
        tts=gTTS("Экспонат №1, Зал №2. Картина Пётра I Алексе́евича, Пётр Вели́кий родился 30 мая 1672, Москва, умер 28 января 1725, в Санкт-Петербурге — царь всея Руси с 1682 года, первый император Всероссийский с 1721 года.", lang="ru", slow=False)
        tts.save(f"{message.from_user.id}.mp3")
        file = open(f"{message.from_user.id}.mp3", 'rb')
        try:
            bot.send_voice(message.chat.id, file, caption="Экспонат №1, Зал №2. Картина Пётра Первого Алексе́евича, Пётр Вели́кий родился 30 мая 1672, Москва, умер 28 января 1725, в"
             "Санкт-Петербурге — царь всея Руси с 1682 года, первый император Всероссийский с 1721 года.")
        finally:
            file.close()
        os.remove(f"{message.from_user.id}.mp3")

    elif message.text == 'Экспонат №2':
        tts=gTTS('"Экспонат №2, Зал №2. Иван Четвёртый Васильевич родился 1530 умер 1584 — государь, царь и великий князь всея Руси с 1533 года, первый венчанный царь всея Руси с 1547 года.',lang="ru",slow=False)
        tts.save(f"{message.from_user.id}.mp3")
        file = open(f"{message.from_user.id}.mp3", 'rb')
        try:
            bot.send_voice(message.chat.id, file, caption='Экспонат №2, Зал №2. Иван IV Васильевич (1530–1584) — государь, царь и великий князь всея Руси с 1533 года, первый венчанный царь всея Руси (с 1547 года).')
        finally:
            file.close()
        os.remove(f"{message.from_user.id}.mp3")

    elif message.text == 'Экспонат №3':
        tts=gTTS("Экспонат №3, Зал №2. Подарок турецкого султана Абдул-Хамида Первого, императрице Екатерине II в 1775 году. Представляет собой украшение" 
             "для лошади инкрустирована дорогим сапфиром и покрыт серебром.",lang="ru",slow=False)
        tts.save(f"{message.from_user.id}.mp3")
        file = open(f"{message.from_user.id}.mp3", 'rb')
        try:
            bot.send_voice(message.chat.id, file,caption="Экспонат №3, Зал №2. Экспонат №3. Подарок турецкого султана Абдул-Хамида Первого, императрице Екатерине II в 1775 году. Представляет собой украшение" 
             "для лошади инкрустирована дорогим сапфиром и покрыт серебром.")
        finally:
            file.close()
        os.remove(f"{message.from_user.id}.mp3")

    elif message.text == 'Экспонат №4':
        tts=gTTS('Экспонат №4, Зал №2. Учебник который был написан великил учёным нашего времени.',lang="ru",slow=False)
        tts.save(f"{message.from_user.id}.mp3")
        file = open(f"{message.from_user.id}.mp3", 'rb')
        try:
            bot.send_voice(message.chat.id, file,caption='Экспонат №4, Зал №2. Учебник который был написан великим учённым нашего времени.')
        finally:
            file.close()
        os.remove(f"{message.from_user.id}.mp3")  


bot.stop_polling()
bot.polling(none_stop=True)