import aiohttp
import asyncio

async def fetch_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

class News:
    def __init__(self, title: str, desc: str, url: str, code: str) -> None:
        self.title = title
        self.desc = desc
        self.url = url
        self.code = code
    def __repr__(self):
        return self.code

async def map(request):
    BASE_URL = 'https://newsapi.org/v2/everything' 
    apikey = 'dbc06277764c411d84f4cdf4187d8f8c'
    keyword = request
    results = 5

    data = await fetch_json(f"{BASE_URL}?q={keyword}&apikey={apikey}")

    list = []
     
    
    for i in range(results):
        title = data['articles'][i]['title']
        desc = data['articles'][i]['description']
        url = data['articles'][i]['url']
        code = title + ' ' + desc + ' ' + url

        news = News(title, desc, url, code)
        list.append(news)
    

    print(repr(list))
    
    return list

asyncio.run(map('иран'))

