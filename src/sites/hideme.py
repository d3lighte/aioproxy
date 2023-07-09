from aiohttp import ClientSession
from bs4 import BeautifulSoup

async def getProxyMe():
        async with ClientSession(headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:114.0) Gecko/20100101 Firefox/114.0"}) as session:
            async with session.get(url = 'https://hidemy.name/ru/proxy-list/#list') as response:
                text = await response.text()
        soup = BeautifulSoup(text, 'lxml')
        pages = []
        for tr in soup.find_all('tr'):
            page = []
            for td in tr:
                page.append(td.text)
            pages.append(page)
        proxy = []
        for page in pages:
            if 'Порт' not in page:
                 proxy.append([page[0], page[1]])
        proxies = []
        for prx in proxy:
             proxies.append(f'{prx[0]}:{prx[1]}')
        return proxies