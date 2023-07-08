from aiohttp import ClientSession
from random import choice
import aiofiles
import sites
from asyncio import gather

async def getRandom():
    random = await sites.getProxyFPL(), await sites.getProxyGN(), await sites.getProxyMe(), await sites.getProxySsl(), await sites.getProxyUS()
    return choice(choice(random))

async def getAll():
    proxies = []
    prx = []
    proxy_lists = [sites.getProxyFPL(), sites.getProxyGN(), sites.getProxyMe(), sites.getProxySsl(), sites.getProxyUS()]
    for proxy_list in await gather(*proxy_lists):
        proxies.append(proxy_list) 
    for proxy in proxies:
         if proxy != None:
           for pp in proxy:
            prx.append(pp)  
    return prx

async def writeAll(path):
    proxies = await getAll()
    s = ''
    for proxy in proxies:
        s += f'{proxy}\n'
    async with aiofiles.open(path, 'w') as f:
        await f.write(s)

async def checkAll():
    prx = []
    proxies = await getAll()
    tasks = []
    for proxy in proxies:
                async def check(proxy):
                    try:
                        async with ClientSession() as session:
                            async with session.get('https://google.com', proxy=f'http://{proxy}', timeout=10) as response:
                                if response.status == 200:
                                    prx.append(proxy)
                    except:
                        pass
                tasks.append(check(proxy))
        
    await gather(*tasks)
    
    return prx