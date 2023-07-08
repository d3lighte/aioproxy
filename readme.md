#  simple proxy parser with asyncio support.

## dependenciens
Install dependenciens
```
pip install -r requirements.txt
```
## usage
aioproxy.getRandom() - return 1 random proxy
aioproxy.getAll() - return all proxy in list
aioproxy.writeAll(filepath) - write all proxy in your file
aioproxy.checkAll() - check all proxy from getAll()
### Usage example
```
from aioproxy import getRandom, getAll, writeAll, checkAll
from asyncio import run

async def printallproxy()
  print(await getAll) ## [1.1.1.1:80, 22.2.2.2:666, etc]

async def randomproxy()
  print(await getRandom())  ## example 1.1.1.1:8080

async def check()
  proxies = await checkAll()
  for proxy in proxies:
    print(f'{proxy} - is valid')
async def write()
  await writeAll('data/myproxy.txt')

run(write())
```

#### Usage example 2
```
from asyncio import run
from aioproxy import getRandom
from aiohttp import ClientSession

async def request()
  proxy = getRandom()
  async with ClientSession() as session:
    async with session.get('https://example.com', proxy=f'http://{proxy)' as response:
      print(response.status)

run(request())
```
