from email import message
import aiogram
from io import BytesIO
from aiogram import F, Router, Bot, Dispatcher, types
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from gtts import gTTS
import os
import app.keyboards as kb
from aiogram.types.input_file import FSInputFile

from app import bot as bt
from aiogram.types import FSInputFile,BufferedInputFile

from app import router
@router.message(Command('старт'))
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать в наш музей!' 
                         'Выберите зал в котором вы хотите начать экскрсию.', 
                         reply_markup=kb.main)

@router.message(Command('помощь'))
async def cmd_help(message: Message):
    await message.answer('Просто введите номер экспонат, которй вас интерисует'
                         'Номер экспоната будет предоставлен в виде бумажки с номером рядом с экспонатом.')

#Перевод текста в голсо
# def Echo(text):
#     tts = gTTS(text,lang="ru")  
#     tts.save("messag3e.mp3")  
#     voice_data = BytesIO()
#     tts.write_to_fp(voice_data)
#     voice = aiogram.types.InputFile(voice_data, filename="message.mp3")
#     voice.read(bot=bt)
#     return voice
    
    


#Зал №1
@router.message(F.text == 'Зал №1')
async def Hall_No_1(message: Message):
    await message.answer('Выберите номер экспоната, которй вас интересует в "Зал №1"', reply_markup=kb.Hall_No_1)

@router.callback_query(F.data == 'Esponyat No.1')
async def Esponyat_No_1(callback: CallbackQuery):
    await callback.answer('Вы выбрали экспонат')
    # await callback.message.answer(text='Первый экспонат. Это картина великого имера России, Петра I.'
    #                               'Выдающийся человек и тот самый человек, который прорубил окно в Евроау,'
    #                               'и основал кореблестроение в России!')
    tts=gTTS('Первый экспонат. Это картина великого имера России, Петра I.'
                                  'Выдающийся человек и тот самый человек, который прорубил окно в Евроау,'
                                  'и основал кореблестроение в России!',lang="ru",slow=False)
    tts.save(f"{callback.from_user.id}.mp3")
    file=FSInputFile(f"{callback.from_user.id}.mp3")
    await callback.message.answer_voice(voice=file,caption='Первый экспонат. Это картина великого имера России, Петра I.'
                                  'Выдающийся человек и тот самый человек, который прорубил окно в Евроау,'
                                  'и основал кореблестроение в России!')


@router.callback_query(F.data == 'Esponyat No.2')
async def Esponyat_No_2(callback: CallbackQuery):
    await callback.answer('Вы выбрвли экспонат')
    tts=gTTS('Второй экспонат. Это доспехи великого полководца Англии 1843 года.',lang="ru",slow=False)
    tts.save(f"{callback.from_user.id}.mp3")
    file=FSInputFile(f"{callback.from_user.id}.mp3")
    await callback.message.answer_voice(voice=file,caption='Второй экспонат. Это доспехи великого полководца Англии 1843 года.')
    os.remove(f"{callback.from_user.id}.mp3")

@router.callback_query(F.data == 'Esponyat No.3')
async def Esponyat_No_3(callback: CallbackQuery):
    await callback.answer('Вы выбрвли экспонат')
    await callback.message.answer('Вы выбрвли "Экспонат №3"')

@router.callback_query(F.data == 'Esponyat No.4')
async def Esponyat_No_4(callback: CallbackQuery):
    await callback.answer('Вы выбрвли экспонат')
    await callback.message.answer('Вы выбрвли "Экспонат №4"')


#Зал №2
@router.message(F.text == 'Зал №2')
async def Hall_No_2(message: Message):
    await message.answer('Выберите номер экспоната, которй вас интересует в "Зал №2"', reply_markup=kb.Hall_No_2)

@router.callback_query(F.data == 'Esponyat No.1.2')
async def Esponyat_No_1(callback: CallbackQuery):
    await callback.answer('Вы выбрвли экспонат')
    await callback.message.answer('Вы выбрвли "Экспонат №1"')

@router.callback_query(F.data == 'Esponyat No.2.2')
async def Esponyat_No_2(callback: CallbackQuery):
    await callback.answer('Вы выбрвли экспонат')
    await callback.message.answer('Вы выбрвли "Экспонат №2"')

@router.callback_query(F.data == 'Esponyat No.3.2')
async def Esponyat_No_3(callback: CallbackQuery):
    await callback.answer('Вы выбрвли экспонат')
    await callback.message.answer('Вы выбрвли "Экспонат №3"')

@router.callback_query(F.data == 'Esponyat No.4.2')
async def Esponyat_No_4(callback: CallbackQuery):
    await callback.answer('Вы выбрвли экспонат')
    await callback.message.answer('Вы выбрвли "Экспонат №4"')


#Зал №3
@router.message(F.text == 'Зал №3')
async def Hall_No_3(message: Message):
    await message.answer('Выберите номер экспоната, которй вас интересует в "Зал №3"', reply_markup=kb.Hall_No_3)

@router.callback_query(F.data == 'Esponyat No.1.3')
async def Esponyat_No_1(callback: CallbackQuery):
    await callback.answer('Вы выбрвли экспонат')
    await callback.message.answer('Вы выбрвли "Экспонат №1"')

@router.callback_query(F.data == 'Esponyat No.2.3')
async def Esponyat_No_2(callback: CallbackQuery):
    await callback.answer('Вы выбрвли экспонат')
    await callback.message.answer('Вы выбрвли "Экспонат №2"')

@router.callback_query(F.data == 'Esponyat No.3.3')
async def Esponyat_No_3(callback: CallbackQuery):
    await callback.answer('Вы выбрвли экспонат')
    await callback.message.answer('Вы выбрвли "Экспонат №3"')

@router.callback_query(F.data == 'Esponyat No.4.3')
async def Esponyat_No_4(callback: CallbackQuery):
    await callback.answer('Вы выбрвли экспонат')
    await callback.message.answer('Вы выбрвли "Экспонат №4"')


#Зал №4
@router.message(F.text == 'Зал №4')
async def Hall_No_4(message: Message):
    await message.answer('Выберите номер экспоната, которй вас интересует в "Зал №4"', reply_markup=kb.Hall_No_4)

@router.callback_query(F.data == 'Esponyat No.1.4')
async def Esponyat_No_1(callback: CallbackQuery):
    await callback.answer('Вы выбрвли экспонат')
    await callback.message.answer('Вы выбрвли "Экспонат №1"')

@router.callback_query(F.data == 'Esponyat No.2.4')
async def Esponyat_No_2(callback: CallbackQuery):
    await callback.answer('Вы выбрвли экспонат')
    await callback.message.answer('Вы выбрвли "Экспонат №2"')

@router.callback_query(F.data == 'Esponyat No.3.4')
async def Esponyat_No_3(callback: CallbackQuery):
    await callback.answer('Вы выбрвли экспонат')
    await callback.message.answer('Вы выбрвли "Экспонат №3"')

@router.callback_query(F.data == 'Esponyat No.4.4')
async def Esponyat_No_4(callback: CallbackQuery):
    await callback.answer('Вы выбрвли экспонат')
    await callback.message.answer('Вы выбрвли "Экспонат №4"')

