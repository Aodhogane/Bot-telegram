import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from Token import Token


bot = Bot(token=Token)
dp=Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать в наш музей!')

@dp.message(F.text == '1')
async def The_first_example(message: Message):
    await message.answer('Прямо перед собой сейчас вы видите стол, за которым работал первый директор училища — Максименко Филипп Емельянович.' 
                         'Он был не только директором, но и преподавателем, а еще выдающимся ученым своего времени.' 
                         'Филипп Емельянович является основателем одной из старейших лабораторий в МИИТе — гидравлической.' 
                         'Лаборатория построена и оснащена под его его прямым руководством, а уникальная гидравлическая установка выполнена по его проекту на Бутырском заводе,' 
                         'и действует до сих пор. Увидеть её вы сможете после посещения второго, "Исторического зала".')

async def main():
    await dp.start_polling(bot)


if __name__ =='__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен!')