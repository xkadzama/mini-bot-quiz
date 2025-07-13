from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def make_start_kb() -> ReplyKeyboardMarkup:
    kb = [
        [KeyboardButton(text='Начать викторину!')]
    ]
    return ReplyKeyboardMarkup(keyboard=kb)