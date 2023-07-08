from aiohttp import ClientSession

async def getProxyGN():
    async with ClientSession() as session:
        async with session.get(url = 'https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc') as page:
             page = await page.json()
    proxies = []
    for proxy in page['data']:
        ip, port = proxy['ip'], proxy['port']
        proxies.append(f'{ip}:{port}')
    return proxies    
