import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from site_checker import SiteChecker

TOKEN = "8348856540:AAF20LuE0nwAQkG8TaMKtvH9qqL3eFasZ-I"
bot = Bot(token=TOKEN)
dp = Dispatcher()


# /start
@dp.message(CommandStart())
async def start_handler(message:types.Message):
    await message.answer("Привет! Отправь домен сайта")


# site status check
checker = SiteChecker()

@dp.message()
async def handle_text(message: types.Message):
    domain = message.text.strip()
    await message.answer("Проверяю сайт...")
    result = await checker.check(domain)
    
    await message.answer(f"{domain} -> {result}")



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())