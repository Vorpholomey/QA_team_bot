from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from config_date import config
from config_date.config import Config, load_config
from keyboard.keyboards import create_key
from lexicon_ru import LEXICON_MENU, LEXICON_TIME

config: Config = load_config()
chat_id = config.tg_chat.tg_chat_id
main_chat_id = config.tg_main_chat.tg_main_chat_id


router: Router = Router()
keyboard_start = create_key(2, **LEXICON_MENU)

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer('Погнали.. ', reply_markup=keyboard_start)

@router.message(Command("время"))
async def deach(message: Message, bot: Bot):
    await bot.send_message(main_chat_id, LEXICON_TIME['time'])

@router.message(Command("душно"))
async def deach(message: Message, bot: Bot):
    await bot.send_message(main_chat_id, LEXICON_TIME['window'])

@router.message(Command("пока"))
async def deach(message: Message, bot: Bot):
    await bot.send_message(main_chat_id, LEXICON_TIME['bye'])

@router.message(Command("предупреждение"))
async def deach(message: Message, bot: Bot):
    await bot.send_message(main_chat_id, LEXICON_TIME['notification'])