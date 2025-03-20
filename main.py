import asyncio
import logging
import keep_alive
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.client.bot import DefaultBotProperties

TOKEN = "7013565773:AAHT952nAfTZQslkQZi65HU1oKL3ZgpcVD8"  # Твой токен

# Передаем настройки по умолчанию через default
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    text = (
        f"Привет, {message.from_user.first_name}!\n"
        "❗ Это Единственный ОФИЦИАЛЬНЫЙ канал-переходник\n\n"
        "⚡ Остальные каналы, которые представлены в поиске - МОШЕННИКИ!\n\n"
        "📝 Ниже Ссылка на наш закрытый канал.\n\n"
        "✅ Заявки в канал принимаются автоматически!\n\n"
        "https://t.me/+VeGsAspumG9hOTdi\n"
        "https://t.me/+VeGsAspumG9hOTdi\n"
        "https://t.me/+VeGsAspumG9hOTdi\n"
    )
    await message.answer(text)

async def main():
    logging.basicConfig(level=logging.INFO)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
