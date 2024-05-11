import os
import app.keyboards as kb

from aiogram import F 
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from gtts import gTTS
from aiogram.types.input_file import FSInputFile

from app import bot as bt
from aiogram.types import FSInputFile

from app import router

@router.message(F.text == 'Помощь')
async def main(message: Message):
    await message.answer('Введите номер экспонат, которй вас интерисует'
                         'Номер экспоната будет предоставлен в виде бумажки с номером рядом с экспонатом')


#Зал №1
@router.message(F.text == 'Зал №1')
async def Hall_No_1(message: Message):
    await message.answer('Выберите номер экспоната, которй вас интересует в "Зал №1"', reply_markup=kb.Hall_No_1)

@router.callback_query(F.data == 'Esponyat No.1')
async def Esponyat_No_1(callback: CallbackQuery):
    await callback.answer('Вы выбрали экспонат')
    
    tts=gTTS('Экспонат №1. Это картина великого императора России, Петра первого.'
                                  'Выдающийся человек и тот самый, который прорубил окно в Евроау,'
                                  'и основал кораблестроение в России!',lang="ru",slow=False)
    tts.save(f"{callback.from_user.id}.mp3")
    file=FSInputFile(f"{callback.from_user.id}.mp3")
    await callback.message.answer_voice(voice=file,caption='Первый экспонат. Это картина великого имера России, Петра I.'
                                  'Выдающийся человек и тот самый человек, который прорубил окно в Евроау,'
                                  'и основал кораблестроение в России!')
    os.remove(f"{callback.from_user.id}.mp3")

@router.callback_query(F.data == 'Esponyat No.2')
async def Esponyat_No_2(callback: CallbackQuery):
    await callback.answer('Вы выбрвли экспонат')

    tts=gTTS('"Экспонат №2. Это доспехи великого полководца Англии 1843 года.',lang="ru",slow=False)
    tts.save(f"{callback.from_user.id}.mp3")
    file=FSInputFile(f"{callback.from_user.id}.mp3")

    await callback.message.answer_voice(voice=file, caption='Второй экспонат. Это доспехи великого полководца Англии 1843 года.')
    os.remove(f"{callback.from_user.id}.mp3")

@router.callback_query(F.data == 'Esponyat No.3')
async def Esponyat_No_3(callback: CallbackQuery):
    await callback.answer('Вы выбрвли экспонат')

    tts=gTTS('"Экспонат №3. Карта России, 1764 года.',lang="ru",slow=False)
    tts.save(f"{callback.from_user.id}.mp3")
    file=FSInputFile(f"{callback.from_user.id}.mp3")
    await callback.message.answer_voice(voice=file,caption='Третий экспонат. Карта России, 1764 года.')
    os.remove(f"{callback.from_user.id}.mp3")

@router.callback_query(F.data == 'Esponyat No.4')
async def Esponyat_No_4(callback: CallbackQuery):
    await callback.answer('Вы выбрвли экспонат')

    tts=gTTS('Экспонат №4. Учебник который был написан великил учёным нашего времени.',lang="ru",slow=False)
    tts.save(f"{callback.from_user.id}.mp3")
    file=FSInputFile(f"{callback.from_user.id}.mp3")
    await callback.message.answer_voice(voice=file,caption='Экспонат №4. Учебник который был написан великим учённым нашего времени.')
    os.remove(f"{callback.from_user.id}.mp3")

# #Зал №2
# @router.message(F.text == 'Зал №2')
# async def Hall_No_2(message: Message):
#     await message.answer('Выберите номер экспоната, которй вас интересует в "Зал №2"', reply_markup=kb.Hall_No_2)

# @router.callback_query(F.data == 'Esponyat No.1.2')
# async def Esponyat_No_1(callback: CallbackQuery):
#     await callback.answer('Вы выбрвли экспонат')
#     await callback.message.answer('Вы выбрвли "Экспонат №1"')

# @router.callback_query(F.data == 'Esponyat No.2.2')
# async def Esponyat_No_2(callback: CallbackQuery):
#     await callback.answer('Вы выбрвли экспонат')
#     await callback.message.answer('Вы выбрвли "Экспонат №2"')

# @router.callback_query(F.data == 'Esponyat No.3.2')
# async def Esponyat_No_3(callback: CallbackQuery):
#     await callback.answer('Вы выбрвли экспонат')
#     await callback.message.answer('Вы выбрвли "Экспонат №3"')

# @router.callback_query(F.data == 'Esponyat No.4.2')
# async def Esponyat_No_4(callback: CallbackQuery):
#     await callback.answer('Вы выбрвли экспонат')
#     await callback.message.answer('Вы выбрвли "Экспонат №4"')


# #Зал №3
# @router.message(F.text == 'Зал №3')
# async def Hall_No_3(message: Message):
#     await message.answer('Выберите номер экспоната, которй вас интересует в "Зал №3"', reply_markup=kb.Hall_No_3)

# @router.callback_query(F.data == 'Esponyat No.1.3')
# async def Esponyat_No_1(callback: CallbackQuery):
#     await callback.answer('Вы выбрвли экспонат')
#     await callback.message.answer('Вы выбрвли "Экспонат №1"')

# @router.callback_query(F.data == 'Esponyat No.2.3')
# async def Esponyat_No_2(callback: CallbackQuery):
#     await callback.answer('Вы выбрвли экспонат')
#     await callback.message.answer('Вы выбрвли "Экспонат №2"')

# @router.callback_query(F.data == 'Esponyat No.3.3')
# async def Esponyat_No_3(callback: CallbackQuery):
#     await callback.answer('Вы выбрвли экспонат')
#     await callback.message.answer('Вы выбрвли "Экспонат №3"')

# @router.callback_query(F.data == 'Esponyat No.4.3')
# async def Esponyat_No_4(callback: CallbackQuery):
#     await callback.answer('Вы выбрвли экспонат')
#     await callback.message.answer('Вы выбрвли "Экспонат №4"')


# #Зал №4
# @router.message(F.text == 'Зал №4')
# async def Hall_No_4(message: Message):
#     await message.answer('Выберите номер экспоната, которй вас интересует в "Зал №4"', reply_markup=kb.Hall_No_4)

# @router.callback_query(F.data == 'Esponyat No.1.4')
# async def Esponyat_No_1(callback: CallbackQuery):
#     await callback.answer('Вы выбрвли экспонат')
#     await callback.message.answer('Вы выбрвли "Экспонат №1"')

# @router.callback_query(F.data == 'Esponyat No.2.4')
# async def Esponyat_No_2(callback: CallbackQuery):
#     await callback.answer('Вы выбрвли экспонат')
#     await callback.message.answer('Вы выбрвли "Экспонат №2"')

# @router.callback_query(F.data == 'Esponyat No.3.4')
# async def Esponyat_No_3(callback: CallbackQuery):
#     await callback.answer('Вы выбрвли экспонат')
#     await callback.message.answer('Вы выбрвли "Экспонат №3"')

# @router.callback_query(F.data == 'Esponyat No.4.4')
# async def Esponyat_No_4(callback: CallbackQuery):
#     await callback.answer('Вы выбрвли экспонат')
#     await callback.message.answer('Вы выбрвли "Экспонат №4"')

