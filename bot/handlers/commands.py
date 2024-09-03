from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

router = Router()


@router.message(CommandStart())
async def start_message(message: Message):
    await message.answer(text="Приветсвенное сообщение")
