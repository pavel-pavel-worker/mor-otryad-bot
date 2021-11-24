from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from bot.phrases import reply_keyboards
from bot.phrases.reply_keyboards import reply_keyboard_texts
from bot.phrases.responses import bot_responses
from bot import utils
from bot.correct import get_correct_word
from bot.exceptions import CantGetDefinition


class GetCorrect(StatesGroup):
    word = State()
    verification = State()


async def start_get_correct(message: types.Message, state: FSMContext):
    bot_message = await message.answer(text=bot_responses['get correct']['enter'],
                                       reply_markup=types.ReplyKeyboardRemove())
    await GetCorrect.word.set()


async def process_word(message: types.Message, state: FSMContext):
    word = message.text.strip().lower()
    try:
        answer_text = get_correct_word(word)
    except CantGetDefinition:
        await utils.process_error(CantGetDefinition(), message, state)
        return
    await message.answer(text=answer_text, reply_markup=reply_keyboards.menu)
    await message.answer(text=bot_responses['get correct']['end'], reply_markup=reply_keyboards.verification)
    await GetCorrect.verification.set()


async def process_verification_is_ok(message: types.Message, state: FSMContext):
    bot_message = await message.answer(text=bot_responses['verification']['ok'], reply_markup=reply_keyboards.menu)
    await state.finish()


async def process_verification_is_not_ok(message: types.Message, state: FSMContext):
    fact = utils.get_fact()
    if fact[0] == 'fact':
        bot_message = await message.answer(text=bot_responses['verification']['not ok fact'].format(fact=fact[1]),
                                           reply_markup=reply_keyboards.menu)
    else:
        bot_message = await message.answer(text=bot_responses['verification']['not ok sayings'].format(sayings=fact[1]),
                                           reply_markup=reply_keyboards.menu)
    await state.finish()


def register_handlers_get_correct(dp: Dispatcher):
    dp.register_message_handler(start_get_correct,
                                Text(equals=reply_keyboard_texts['menu']['get correct'], ignore_case=True))
    dp.register_message_handler(process_word, state=GetCorrect.word)
    dp.register_message_handler(process_verification_is_ok,
                                Text(equals=reply_keyboard_texts['verification']['ok'], ignore_case=True),
                                state=GetCorrect.verification)
    dp.register_message_handler(process_verification_is_not_ok,
                                Text(equals=reply_keyboard_texts['verification']['not ok'], ignore_case=True),
                                state=GetCorrect.verification)
