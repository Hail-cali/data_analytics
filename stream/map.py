
# python 3.8
import asyncio
import requests
from queue import PriorityQueue
import time

TIMEOUT = 3000

class BaseSession:

    def __init__(self, base=requests, url=None, *args):
        self.url = url
        self.request = base

    async def __aenter__(self, *args):
        # print('enter ')

        return self.request.get(self.url)

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # print('end reader')
        pass

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

        print(f'reserved : {len(self._schedule)} ', end=' ')


    def executor(self):
        print('>> execute')
        return self._schedule


    @staticmethod
    def check_status(reader):

        if isinstance(reader, BaseReader):
            return True

        else:
            return False



class BaseReader:

    def __init__(self, session=requests, timeout=TIMEOUT):
        self.session = session
        self._urls = None
        self.timeout = timeout

    async def __aenter__(self, *args):


        pass

    async def __aexit__(self, exc_type, exc_val, exc_tb):

        return self

    @property
    def urls(self):
        return self._urls

    @urls.setter
    def urls(self, query):
        self._urls = query


    async def request(self, url=None):

        if url is not None:
            self.urls = url


        if issubclass(self.session, BaseSession):

            async with self.session(requests, url) as response:

                text = response.text

                # print(f'URL: {self.url}\nTEXT {text[30:60]}')
                return text

        else:

            with self.session.get(url) as response:

                text = response.text

                print(f'URL: {url}\nTEXT {text[30:60]}')
                return text


class BaseWriter:

    pass

