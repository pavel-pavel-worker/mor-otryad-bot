import yaml
from aiogram import Dispatcher, types

with open('bot/phrases/commands.yaml', encoding='utf-8') as yaml_file:
    commands = yaml.safe_load(yaml_file)


async def set_commands(dp: Dispatcher):
    global commands
    bot_commands = [
        types.BotCommand(command=f'{command}', description=commands[command])
        for command in commands
    ]
    await dp.bot.set_my_commands(bot_commands)
