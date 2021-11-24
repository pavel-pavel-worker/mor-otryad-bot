from bot.bot import bot
from typing import List
from random import choices, choice

from aiogram import types
from aiogram.dispatcher import FSMContext
from bot.phrases import reply_keyboards
from bot.phrases.responses import bot_responses


async def delete_messages(chat_id: int, message_ids: List[int]):
    for message_id in message_ids:
        await bot.delete_message(chat_id, message_id)


async def process_error(error: Exception, message: types.Message, state: FSMContext):
    await message.answer(text=bot_responses['error'].format(error=error),
                         reply_markup=reply_keyboards.menu,
                         parse_mode='Markdown')
    await state.finish()


async def save_message_ids(state, message, bot_message):
    data = await state.get_data()
    await state.update_data(message_ids=data.get('message_ids', []) + [message.message_id, bot_message.message_id])


with open('facts.txt', encoding='utf-8') as file:
    facts = [line for line in file.read().split('\n') if line]

with open('sayings.txt', encoding='utf-8') as file:
    sayings = [line for line in file.read().split('\n') if line]


def get_fact():
    type_ = choice(['fact', 'saying'])
    if type_ == 'fact':
        result = choices(facts)[0]
    else:
        result = '\n'.join(set(choices(sayings, k=5)))
    return type_, result
