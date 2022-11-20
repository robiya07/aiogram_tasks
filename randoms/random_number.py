import logging
from aiogram import Bot, Dispatcher, executor, types

from random import seed, choice, randint

API_TOKEN = '5539016910:AAE0QLol57MMWA65-G0dxu-F69exdXlS-B4'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

s = []

seed(1)


@dp.message_handler(commands=['generate'])
async def num(msg: types.Message):
    await msg.answer('Enter the starting number')

    @dp.message_handler()
    async def start(msg: types.Message):
        if msg.text.isdigit():
            s.append(int(msg.text))
        else:
            await msg.answer('Please enter a number!')
        if len(s) == 1:
            await msg.answer('Enter the ending number')
            if msg.text.isdigit():
                s.append(int(msg.text))
            else:
                await msg.answer('Please enter a number!')
        if len(s) >= 2:
            # value = randint(min(s), max(s))
            f = [i for i in range(min(s), max(s))]
            selection = choice(f)
            await msg.answer(f"You're random number is {selection}")
            f.clear()
            s.clear()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

