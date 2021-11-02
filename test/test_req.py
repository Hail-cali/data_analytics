import asyncio
from stream.map import BaseReader


async def wrapper(func):
    await asyncio.wait([func])

def sub():
    import requests
    URL = 'https://www.google.co.kr/search?q=apple'
    result = requests.get(URL)
    print(result.text)

def main():
    URL = 'https://www.google.co.kr/search?q=apple'
    b = BaseReader(url=URL)



if __name__ == '__main__':
    # sub()
    main()