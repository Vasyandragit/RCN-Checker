import asyncio
from weakref import proxy
import aiohttp


#ru_proxy = "http://188.191.164.55"
class SiteChecker:
    async def check(self, domain: str):
        url = f"http://{domain}"

        try:
            timeout = aiohttp.ClientTimeout(total=5)

            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.get(url) as response:
                    return {
                        "status" : "ok",
                        "code" : response.status
                    }

        except asyncio.TimeoutError:
            return {"status" : "timeout"}

        except aiohttp.ClientError:
            return {"status" : "down"}

        except Exception as e:
            return {"status" : "error", "detail" : str(e)}