from aiogram import Dispatcher, types, filters
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from bot.phrases.reply_keyboards import reply_keyboard_texts
from bot.phrases import reply_keyboards
from bot.handlers.get_definition import register_handlers_get_definition
from bot.handlers.get_accent import register_handlers_get_accent
from bot.handlers.get_correct import register_handlers_get_correct
from bot.phrases.responses import bot_responses


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'], state='*')
    dp.register_message_handler(about, commands=['about'], state='*')
    dp.register_message_handler(feedback, commands=['feedback'], state='*')
    register_handlers_get_definition(dp)
    register_handlers_get_accent(dp)
    register_handlers_get_correct(dp)
    dp.register_message_handler(wtf)


async def start(message: types.Message):
    await message.answer(text=bot_responses['start'], reply_markup=reply_keyboards.menu)


async def about(message: types.Message):
    await message.answer(text=bot_responses['about'])


async def feedback(message: types.Message):
    await message.answer(text=bot_responses['feedback'])


async def wtf(message: types.Message):
    await message.answer(text='чо', reply_markup=reply_keyboards.menu)
