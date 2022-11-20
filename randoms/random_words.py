import logging
from aiogram import Bot, Dispatcher, executor, types

from random import seed, choice, randint

from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '5539016910:AAE0QLol57MMWA65-G0dxu-F69exdXlS-B4'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

with open('words.txt', 'r') as file:
    word = file.readlines()

with open('nouns.txt', 'r') as file1, open('adjectives.txt', 'r') as file2:
    noun = file1.readlines()
    adjective = file2.readlines()

with open('verbs.txt', 'r') as file3, open('pronouns.txt', 'r') as file4:
    verb = file3.readlines()
    pronoun = file4.readlines()

seed(1)
s = []


@dp.message_handler(commands=['generate'])
async def num(msg: types.Message):
    ikm = InlineKeyboardMarkup(row_width=2)
    ikm.add(
        InlineKeyboardButton('noun', callback_data='noun'),
        InlineKeyboardButton('adjective', callback_data='adjective'),
        InlineKeyboardButton('verb', callback_data='verb'),
        InlineKeyboardButton('pronoun', callback_data='pronoun'),
        InlineKeyboardButton('all', callback_data='all')
    )
    await msg.answer('Choose the button or enter the necessary command', reply_markup=ikm)


@dp.callback_query_handler(Text(startswith='all'))
async def noun_(msg: types.CallbackQuery):
    await msg.message.answer('Enter the length of random word')

    @dp.message_handler()
    async def start(msg: types.Message):
        all_word = []
        if msg.text.isdigit():
            s.append(int(msg.text))
        else:
            await msg.answer('Please enter a number!')
        for i in word:
            if len(i) == s[0] + 1:
                all_word.append(i)
        if len(s) == 1:
            selection = choice(all_word)
            await msg.answer(f"Randomly word: {selection}")
            s.clear()
            all_word.clear()


@dp.callback_query_handler(Text(startswith='noun'))
async def noun_(msg: types.CallbackQuery):
    await msg.message.answer('Enter the length of random word')

    @dp.message_handler()
    async def start(msg: types.Message):
        n_word = []
        if msg.text.isdigit():
            s.append(int(msg.text))
        else:
            await msg.answer('Please enter a number!')
        for i in noun:
            if len(i) == s[0] + 1:
                n_word.append(i)
        if len(s) == 1:
            selection = choice(n_word)
            await msg.answer(f"Randomly word: {selection}")
            s.clear()
            n_word.clear()


@dp.callback_query_handler(Text(startswith='adjective'))
async def adj_(msg: types.CallbackQuery):
    await msg.message.answer('Enter the length of random word')

    @dp.message_handler()
    async def start(msg: types.Message):
        a_word = []
        if msg.text.isdigit():
            s.append(int(msg.text))
        else:
            await msg.answer('Please enter a number!')
        for i in adjective:
            if len(i) == s[0] + 1:
                a_word.append(i)
        if len(s) == 1:
            selection = choice(a_word)
            await msg.answer(f"Randomly word: {selection}")
            s.clear()
            a_word.clear()


@dp.callback_query_handler(Text(startswith='verb'))
async def verb_(msg: types.CallbackQuery):
    await msg.message.answer('Enter the length of random word')

    @dp.message_handler()
    async def start(msg: types.Message):
        v_word = []
        if msg.text.isdigit():
            s.append(int(msg.text))
        else:
            await msg.answer('Please enter a number!')
        for i in verb:
            if len(i) == s[0] + 1:
                v_word.append(i)
        if len(s) == 1:
            selection = choice(v_word)
            await msg.answer(f"Randomly word: {selection}")
            s.clear()
            v_word.clear()


@dp.callback_query_handler(Text(startswith='pronoun'))
async def pro_(msg: types.CallbackQuery):
    await msg.message.answer('Enter the length of random word')

    @dp.message_handler()
    async def start(msg: types.Message):
        p_word = []
        if msg.text.isdigit():
            s.append(int(msg.text))
        else:
            await msg.answer('Please enter a number!')
        for i in pronoun:
            if len(i) == s[0] + 1:
                p_word.append(i)
        if len(s) == 1:
            selection = choice(p_word)
            await msg.answer(f"Randomly word:k {selection}")
            s.clear()
            p_word.clear()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
