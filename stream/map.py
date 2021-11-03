
# python 3.8
import asyncio
import requests
from queue import PriorityQueue
import time

TIMEOUT = 3000

class BaseSession:

    async def __aenter__(self, *args):
        print('enter ')
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print('end reader')
        return self

    def get(self, url):
        return requests.get(url)

class BaseStream:

    def __init__(self, timeout=TIMEOUT, reader=None, writer=None):
        self.reader: BaseReader = reader
        self.writer: BaseWriter = writer
        self._tasks = None
        self.timeout = timeout
        self._schedule = []   # dev modifiy class type list to PrirityQueue

    @property
    def queue(self):
        return PriorityQueue()

    @property
    def tasks(self):
        return self._tasks


    @tasks.setter
    def tasks(self, cls):

        self._tasks = cls


    def scheduler(self, url=None):
        if self.check_status(self.reader):
            self._schedule.append(self.reader.request(url))

        else:
            print(f'Check Reader Type: {type(self.reader)}')

        print(f'reserved : {len(self._schedule)} work is scheduled')


    def executor(self):
        return self._schedule


    @staticmethod
    def check_status(reader):

        if isinstance(reader, BaseReader):
            return True

        else:
            return False



class BaseReader:

    def __init__(self, url=None, session=requests, timeout=TIMEOUT):
        self.session = session
        self._url = url
        self.timeout = timeout

    async def __aenter__(self, *args):
        print('enter ')
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print('end reader')
        return self

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, query):
        self._url = query


    async def request(self, url=None):

        if url is not None:
            self.url = url

        with self.session.get(self.url) as response:

            text = response.text

            print(f'URL: {self.url}\nTEXT {text[30:60]}')
            return text

        # async with self.session.get(self.url) as response:
        #
        #     text = response.text
        #
        #     print(f'URL: {self.url}\nTEXT {text[30:60]}')
        #     return text


class BaseWriter:

    pass



if __name__ == '__main__':
    url = 'https://www.google.co.kr/search?q=apple'

    link_list = ['https://www.google.co.kr/search?q=apple','https://www.google.co.kr/search?q=mango',
                 'https://www.google.co.kr/search?q=banana','https://www.google.co.kr/search?q=apple'
                 'https://www.google.co.kr/search?q=kiwi','https://www.google.co.kr/search?q=dev']

    a_start = time.time()

    stream = BaseStream(reader=BaseReader(url=url))
    for l in link_list:
        stream.scheduler(url=l)

    asyncio.run(asyncio.wait(stream.executor()))
    a_end = time.time()

    print(f'asyncio {a_end-a_start:.5f}times')
    b_start = time.time()

    for l in link_list:
        print(requests.get(l).text[100:150])
    b_end = time.time()

    print(f'python {b_end-b_start:.5f} times')

    # requests.get(url)
    print()