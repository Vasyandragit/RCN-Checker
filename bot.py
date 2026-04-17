import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from site_checker import SiteChecker
from news_parser import NewsParser


TOKEN = "8348856540:AAF20LuE0nwAQkG8TaMKtvH9qqL3eFasZ-I"
bot = Bot(token=TOKEN)
dp = Dispatcher()


# /start
@dp.message(CommandStart())
async def start_handler(message:types.Message):
    await message.answer("Привет! Отправь домен сайта")


# site status check + news check
checker = SiteChecker()
parser = NewsParser()


# user domain handling
@dp.message()
async def handle_text(message: types.Message):
    domain = message.text.strip()
    
    await message.answer("Проверяю сайт...")
    status_result = await checker.check(domain)
    await message.answer(f"{domain} -> {status_result}")

    await message.answer("Ищу новости...")
    news_list = await parser.get_news(f"{domain[:domain.rfind('.')]}")

    if not news_list:
        await message.answer("Новости не найдены")
        return

    for news in news_list:
        if "блок" in news["title"].lower():
            text = (
                f"📰 {news["title"]}\n"
                f"{news["desc"]}\n"
                f"{news["url"]}\n"
            )
            await message.answer(text)

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())