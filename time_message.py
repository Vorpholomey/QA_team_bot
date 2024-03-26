from datetime import datetime

from aiogram import Bot

from config_date.config import Config, load_config
from lexicon_ru import LEXICON_TIME

config: Config = load_config()
chat_id = config.tg_chat.tg_chat_id
main_chat_id = config.tg_main_chat.tg_main_chat_id

async def send_message_time(bot:Bot):
    await bot.send_message(main_chat_id,LEXICON_TIME['time'])


async def send_message_window(bot:Bot):
    await bot.send_message(main_chat_id,LEXICON_TIME['window'])


async def send_message_bye(bot:Bot):
    await bot.send_message(main_chat_id,LEXICON_TIME['bye'])

async def send_message_notification(bot:Bot):
  await bot.send_message(main_chat_id,LEXICON_TIME['notification'])

async def send_message_charge(bot:Bot):
  await bot.send_message(main_chat_id,LEXICON_TIME['charge'])