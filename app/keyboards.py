from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Зал №1')],
                                     [KeyboardButton(text='Зал №2')],
                                     [KeyboardButton(text='Зал №3'),
                                     KeyboardButton(text='Зал №4')]],
                            resize_keyboard=True,   
                            input_field_placeholder='Выберите зал...')


Hall_No_1 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Эеспонят №1', callback_data='Esponyat No.1')],
                                                  [InlineKeyboardButton(text='Эеспонят №2', callback_data='Esponyat No.2')],
                                                  [InlineKeyboardButton(text='Эеспонят №3', callback_data='Esponyat No.3')],
                                                  [InlineKeyboardButton(text='Эеспонят №4', callback_data='Esponyat No.4')]])

Hall_No_2 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Эеспонят №1', callback_data='Esponyat No.1.2')],
                                                  [InlineKeyboardButton(text='Эеспонят №2', callback_data='Esponyat No.2.2')],
                                                  [InlineKeyboardButton(text='Эеспонят №3', callback_data='Esponyat No.3.2')],
                                                  [InlineKeyboardButton(text='Эеспонят №4', callback_data='Esponyat No.4.2')]])

Hall_No_3 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Эеспонят №1', callback_data='Esponyat No.1.3')],
                                                  [InlineKeyboardButton(text='Эеспонят №2', callback_data='Esponyat No.2.3')],
                                                  [InlineKeyboardButton(text='Эеспонят №3', callback_data='Esponyat No.3.3')],
                                                  [InlineKeyboardButton(text='Эеспонят №4', callback_data='Esponyat No.4.3')]])

Hall_No_4 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Эеспонят №1', callback_data='Esponyat No.1.4')],
                                                  [InlineKeyboardButton(text='Эеспонят №2', callback_data='Esponyat No.2.4')],
                                                  [InlineKeyboardButton(text='Эеспонят №3', callback_data='Esponyat No.3.4')],
                                                  [InlineKeyboardButton(text='Эеспонят №4', callback_data='Esponyat No.4.4')]])
