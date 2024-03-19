from datetime import datetime
from environs import Env
from aiogram import Bot
from lexicon_ru import LEXICON_TIME

chat_id = env('CHAT_ID')
main_chat_id = env('MAIN_CHAT_ID')

async def send_message_time(bot:Bot):
    await bot.send_message(main_chat_id,LEXICON_TIME['time'])


async def send_message_window(bot:Bot):
    await bot.send_message(main_chat_id,LEXICON_TIME['window'])


async def send_message_bye(bot:Bot):
    await bot.send_message(main_chat_id,LEXICON_TIME['bye'])

async def send_message_notification(bot:Bot):
  await bot.send_message(main_chat_id,LEXICON_TIME['notification'])
