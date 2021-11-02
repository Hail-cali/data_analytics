
# python 3.8
import asyncio
import requests


TIMEOUT = 3000

class BaseStream:
    pass


class BaseReader:

    def __init__(self, url, session=requests, timeout=TIMEOUT):
        self.session = session
        self.url = url
        self.timeout = timeout


    async def __aenter__(self):

        await asyncio.sleep(1.0)

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print('end reader')
        pass


    async def request(self):
        '''

        :return: https request
        '''

        async with self.session.get(self.url) as response:
            text = response.text
            print(f'URL: {self.url}\nTEXT {text}')
            return text



