import logging
import os
from aiohttp import web
from urllib.parse import urljoin

from aiogram.dispatcher.webhook import get_new_configured_app
from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from bot.middlewares import InformationMiddleware
from bot.phrases.commands import set_commands
from bot.handlers.handlers import register_handlers
from bot.bot import bot

logging.basicConfig(level=logging.INFO)

dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(InformationMiddleware())
register_handlers(dp)


PROJECT_NAME = os.getenv('PROJECT_NAME')  # Set it as you've set TOKEN env var

WEBHOOK_HOST = f'https://{PROJECT_NAME}.herokuapp.com/'  # Enter here your link from Heroku project settings
WEBHOOK_URL_PATH = '/webhook/' + os.getenv('TOKEN_DAL')
WEBHOOK_URL = urljoin(WEBHOOK_HOST, WEBHOOK_URL_PATH)


async def on_startup(application):
    """Simple hook for aiohttp application which manages webhook"""
    await bot.delete_webhook()
    await bot.set_webhook(WEBHOOK_URL)
    await set_commands(dp)


async def shutdown(application):
    await dp.storage.close()
    await dp.storage.wait_closed()


if __name__ == '__main__':
    print('les go')

    app = get_new_configured_app(dispatcher=dp, path=WEBHOOK_URL_PATH)
    app.on_startup.append(on_startup)
    app.on_shutdown(shutdown)
    web.run_app(app, host='0.0.0.0', port=os.getenv('PORT'))
