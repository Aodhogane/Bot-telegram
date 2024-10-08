import telebot
from telebot import types
from Token import Token
import os
from gtts import gTTS

bot = telebot.TeleBot(Token)

# Словарь для отслеживания состояния выбранного зала для каждого пользователя
user_state = {}

# Старт
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add(types.KeyboardButton('Зал №1'))
    keyboard.add(types.KeyboardButton('Зал №2'))
    bot.send_message(message.chat.id, 'Введите номер экспоната, который вас интересует', reply_markup=keyboard)

# Обработка сообщений
@bot.message_handler(content_types=['text'])
def hall_selection(message):
    global user_state
    
    # Обработка выбора зала
    if message.text == 'Зал №1':
        user_state[message.chat.id] = 'Зал №1'
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add(types.KeyboardButton('Экспонат №1'))
        keyboard.add(types.KeyboardButton('Экспонат №2'))
        keyboard.add(types.KeyboardButton('Экспонат №3'))
        keyboard.add(types.KeyboardButton('Экспонат №4'))
        keyboard.add(types.KeyboardButton('Назад'))
        bot.send_message(message.chat.id, 'Выберите номер экспоната, который вас интересует в "Зал №1"', reply_markup=keyboard)

    elif message.text == 'Зал №2':
        user_state[message.chat.id] = 'Зал №2'
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add(types.KeyboardButton('Экспонат №1'))
        keyboard.add(types.KeyboardButton('Экспонат №2'))
        keyboard.add(types.KeyboardButton('Экспонат №3'))
        keyboard.add(types.KeyboardButton('Экспонат №4'))
        keyboard.add(types.KeyboardButton('Назад'))
        bot.send_message(message.chat.id, 'Выберите номер экспоната, который вас интересует в "Зал №2"', reply_markup=keyboard)

    elif message.text == 'Назад':
        start(message)

    # Обработка выбора экспонатов
    elif message.text.startswith('Экспонат №'):
        current_hall = user_state.get(message.chat.id)
        if current_hall:
            handle_exhibit(message, current_hall)

def handle_exhibit(message, hall):
    exhibit_info = {
        'Зал №1': {
            'Экспонат №1': "Экспонат №1, Зал №1. Картина Пётра I Алексе́евича, Пётр Вели́кий родился 30 мая 1672, Москва, умер 28 января 1725, в Санкт-Петербурге — царь всея Руси с 1682 года, первый император Всероссийский с 1721 года.",
            'Экспонат №2': "Экспонат №2, Зал №1. Иван Четвёртый Васильевич родился 1530 умер 1584 — государь, царь и великий князь всея Руси с 1533 года, первый венчанный царь всея Руси с 1547 года.",
            'Экспонат №3': "Экспонат №3, Зал №1. Подарок турецкого султана Абдул-Хамида Первого, императрице Екатерине II в 1775 году. Представляет собой украшение для лошади, инкрустированное дорогим сапфиром и покрытое серебром.",
            'Экспонат №4': "Экспонат №4, Зал №1. Учебник, который был написан великим учёным нашего времени."
        },
        'Зал №2': {
            'Экспонат №1': "Экспонат №1, Зал №2. Картина Пётра I Алексе́евича, Пётр Вели́кий родился 30 мая 1672, Москва, умер 28 января 1725, в Санкт-Петербурге — царь всея Руси с 1682 года, первый император Всероссийский с 1721 года.",
            'Экспонат №2': "Экспонат №2, Зал №2. Иван Четвёртый Васильевич родился 1530 умер 1584 — государь, царь и великий князь всея Руси с 1533 года, первый венчанный царь всея Руси с 1547 года.",
            'Экспонат №3': "Экспонат №3, Зал №2. Подарок турецкого султана Абдул-Хамида Первого, императрице Екатерине II в 1775 году. Представляет собой украшение для лошади, инкрустированное дорогим сапфиром и покрытое серебром.",
            'Экспонат №4': "Экспонат №4, Зал №2. Учебник, который был написан великим учёным нашего времени."
        }
    }

    exhibit_text = exhibit_info[hall][message.text]
    tts = gTTS(exhibit_text, lang="ru", slow=False)
    tts.save(f"{message.from_user.id}.mp3")
    file = open(f"{message.from_user.id}.mp3", 'rb')
    try:
        bot.send_voice(message.chat.id, file, caption=exhibit_text)
    finally:
        file.close()
        os.remove(f"{message.from_user.id}.mp3")

bot.polling(none_stop=True)
