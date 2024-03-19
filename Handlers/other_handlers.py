from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import CommandStart, Text
from keyboard.keyboards import create_key
from lexicon_ru import LEXICON_MENU, LEXICON_TIME

chat_id = env('CHAT_ID')
main_chat_id = env('MAIN_CHAT_ID')

router: Router = Router()
keyboard_start = create_key(1, **LEXICON_MENU)

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