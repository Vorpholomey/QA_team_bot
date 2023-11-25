from datetime import datetime

from aiogram import Bot
from lexicon_ru import LEXICON_TIME

chat_id = '-1001860076771'

async def send_message_time(bot:Bot):
    await bot.send_message(chat_id,LEXICON_TIME['time'])


async def send_message_window(bot:Bot):
    await bot.send_message(chat_id,LEXICON_TIME['window'])


async def send_message_bye(bot:Bot):
    await bot.send_message(chat_id,LEXICON_TIME['bye'])
