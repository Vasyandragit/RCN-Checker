import aiohttp
import asyncio

class NewsParser:

    async def get_news(self, keyword):
        BASE_URL = "https://newsapi.org/v2/everything" 
        apiKey = "785049a5787047ed81eed7eb03287512"
        results = 100

        async with aiohttp.ClientSession() as session:
            async with session.get(f"{BASE_URL}?q={keyword}&apikey={apiKey}") as response:
                data = await response.json()

        news_list = []
     
        print(data)
        for article in data["articles"][:results]:
            title = article["title"]
            desc = article["description"]
            url = article["url"]

            news_list.append({
                "title" : title,
                "desc" : desc,
                "url" : url
                }) 
    
        return news_list

