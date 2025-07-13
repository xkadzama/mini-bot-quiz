from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from keyboards import make_start_kb

user = Router()

@user.message(CommandStart())
async def start(message: Message):
    await message.answer('Здравствуйте, это бот викторина', reply_markup=make_start_kb())