from aiohttp import ClientSession
from  lxml import html

async def getProxySsl():
    async with ClientSession() as session:
        async with session.get(url = 'https://www.sslproxies.org') as page:
             page = await page.text()
        doc = html.fromstring(page)
        trtabl = doc.xpath('//*[@id="list"]//tr')
        return [f'{trtabl[i][0].text_content()}:{trtabl[i][1].text_content()}'
                    for i in range(1, len(trtabl))]