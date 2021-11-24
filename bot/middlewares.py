"""Аутентификация — пропускаем сообщения только от одного Telegram аккаунта"""
import logging
import yaml
from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from typing import List


class InformationMiddleware(BaseMiddleware):

    @staticmethod
    async def on_pre_process_message(message: types.Message, data: dict):
        print(message.from_user.username, message.from_user.full_name, message.text)
        if False:
            raise CancelHandler()
