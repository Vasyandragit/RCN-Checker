import aiohttp
import asyncio

class NewsParser:

    async def get_news(self, domain):
        BASE_URL = "https://newsapi.org/v2/everything" 
        apiKey = "785049a5787047ed81eed7eb03287512"
        results = 1000

        async with aiohttp.ClientSession() as session:
            async with session.get(f"{BASE_URL}?q={domain}&apikey={apiKey}&language=ru") as response:
                data = await response.json()
        

        news_list = []
        for article in data["articles"][:results]:
            title = article["title"]
            desc = article["description"]
            url = article["url"]

            for keyword in ["блок", "упал", "замедле", "огранич", "недоступ", "сбой"]:
                
                if keyword in title.lower():
                    news_list.append(
                        f"📰 {title}\n"
                        f"{desc}\n"
                        f"{url}\n"
                        )

                    break
    
        return news_list

