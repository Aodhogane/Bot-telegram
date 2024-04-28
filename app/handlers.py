from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

import app.keyboards as kb

router = Router()


@router.message(Command('старт'))
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать в наш музей!' 
                         'Выберите зал в котором вы хотите начать экскрсию.', 
                         reply_markup=kb.main)

@router.message(Command('помощь'))
async def cmd_help(message: Message):
    await message.answer('Просто введите номер экспонат, которй вас интерисует'
                         'Номер экспоната будет предоставлен в виде бумажки с номером рядом с экспонатом.')

#Зал №1
@router.message(F.text == 'Зал №1')
async def Hall_No_1(message: Message):
    await message.answer('Выберите номер экспоната, которй вас интересует в "Зал №1"', reply_markup=kb.Hall_No_1)

@router.callback_query(F.data == 'Esponyat No.1')
async def Esponyat_No_1(callback: CallbackQuery):
    await callback.answer('Вы выбрвли экспонат')
    await callback.message.answer('Вы выбрвли "Экспонат №1"')

@router.callback_query(F.data == 'Esponyat No.2')
async def Esponyat_No_2(callback: CallbackQuery):
    await callback.answer('Вы выбрвли экспонат')
    await callback.message.answer('Вы выбрвли "Экспонат №2"')

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
    await message.answer('Выберите номер экспоната, которй вас интересует в "Зал №1"', reply_markup=kb.Hall_No_2)

@router.callback_query(F.data == 'Esponyat No.1')
async def Esponyat_No_1(callback: CallbackQuery):
    await callback.answer('Вы выбрвли экспонат')
    await callback.message.answer('Вы выбрвли "Экспонат №1"')

@router.callback_query(F.data == 'Esponyat No.2')
async def Esponyat_No_2(callback: CallbackQuery):
    await callback.answer('Вы выбрвли экспонат')
    await callback.message.answer('Вы выбрвли "Экспонат №2"')

@router.callback_query(F.data == 'Esponyat No.3')
async def Esponyat_No_3(callback: CallbackQuery):
    await callback.answer('Вы выбрвли экспонат')
    await callback.message.answer('Вы выбрвли "Экспонат №3"')

@router.callback_query(F.data == 'Esponyat No.4')
async def Esponyat_No_4(callback: CallbackQuery):
    await callback.answer('Вы выбрвли экспонат')
    await callback.message.answer('Вы выбрвли "Экспонат №4"')




#Зал №3
@router.message(F.text == 'Зал №3')
async def Hall_No_3(message: Message):
    await message.answer('Выберите номер экспоната, которй вас интересует в "Зал №1"', reply_markup=kb.Hall_No_3)

@router.callback_query(F.data == 'Esponyat No.1')
async def Esponyat_No_1(callback: CallbackQuery):
    await callback.answer('Вы выбрвли экспонат')
    await callback.message.answer('Вы выбрвли "Экспонат №1"')

@router.callback_query(F.data == 'Esponyat No.2')
async def Esponyat_No_2(callback: CallbackQuery):
    await callback.answer('Вы выбрвли экспонат')
    await callback.message.answer('Вы выбрвли "Экспонат №2"')

@router.callback_query(F.data == 'Esponyat No.3')
async def Esponyat_No_3(callback: CallbackQuery):
    await callback.answer('Вы выбрвли экспонат')
    await callback.message.answer('Вы выбрвли "Экспонат №3"')

@router.callback_query(F.data == 'Esponyat No.4')
async def Esponyat_No_4(callback: CallbackQuery):
    await callback.answer('Вы выбрвли экспонат')
    await callback.message.answer('Вы выбрвли "Экспонат №4"')




#Зал №4
@router.message(F.text == 'Зал №4')
async def Hall_No_4(message: Message):
    await message.answer('Выберите номер экспоната, которй вас интересует в "Зал №1"', reply_markup=kb.Hall_No_4)

@router.callback_query(F.data == 'Esponyat No.1')
async def Esponyat_No_1(callback: CallbackQuery):
    await callback.answer('Вы выбрвли экспонат')
    await callback.message.answer('Вы выбрвли "Экспонат №1"')

@router.callback_query(F.data == 'Esponyat No.2')
async def Esponyat_No_2(callback: CallbackQuery):
    await callback.answer('Вы выбрвли экспонат')
    await callback.message.answer('Вы выбрвли "Экспонат №2"')

@router.callback_query(F.data == 'Esponyat No.3')
async def Esponyat_No_3(callback: CallbackQuery):
    await callback.answer('Вы выбрвли экспонат')
    await callback.message.answer('Вы выбрвли "Экспонат №3"')

@router.callback_query(F.data == 'Esponyat No.4')
async def Esponyat_No_4(callback: CallbackQuery):
    await callback.answer('Вы выбрвли экспонат')
    await callback.message.answer('Вы выбрвли "Экспонат №4"')
