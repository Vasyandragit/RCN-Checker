import asyncio
from weakref import proxy
import aiohttp


ru_proxy = "http://45.91.238.136:39218"
with open("blocked_domains.txt", "r") as f:
    blocked_domains = set(line.strip() for line in f if line.strip())


class SiteChecker:

    async def ping(self, domain : str):
        url = f"http://{domain}"

        try:
            timeout = aiohttp.ClientTimeout(total=5)

            async with aiohttp.ClientSession(timeout=timeout, proxy=ru_proxy) as session:
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


    def rcn_check(self, domain : str) -> bool:
        return domain in blocked_domains
