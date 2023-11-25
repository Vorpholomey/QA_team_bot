from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import CommandStart, Text
from keyboard.keyboards import create_key
from lexicon_ru import LEXICON_MENU, LEXICON_TIME

chat_id = '-1001860076771'

router: Router = Router()
keyboard_start = create_key(1, **LEXICON_MENU)

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer('Погнали.. ', reply_markup=keyboard_start)

@router.message(Text(text='время'))
async def deach(message: Message, bot: Bot):
    await bot.send_message(chat_id, LEXICON_TIME['time'])

@router.message(Text(text='душно'))
async def deach(message: Message, bot: Bot):
    await bot.send_message(chat_id, LEXICON_TIME['window'])

@router.message(Text(text='пока'))
async def deach(message: Message, bot: Bot):
    await bot.send_message(chat_id, LEXICON_TIME['bye'])