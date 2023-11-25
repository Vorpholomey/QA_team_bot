from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def create_key(width: int, *args: str, **kwargs: str):
    menu: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

    buttons: list[KeyboardButton] = []

    if args:
        for button in args:
            buttons.append(KeyboardButton(text=button))

    if kwargs:
        for key, val in kwargs.items():
            buttons.append(KeyboardButton(text=val))

    menu.row(*buttons, width=width)
    return menu.as_markup()