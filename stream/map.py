
# python 3.8
import asyncio
import requests
from queue import PriorityQueue
import time
from bs4 import BeautifulSoup

TIMEOUT = 3000


class BaseSession:

    def __init__(self, base=requests, url=None, *args):
        self.url = url
        self.request = base

    async def __aenter__(self, *args):
        print('enter ')

        res = self.request.get(self.url)

        return res.text

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print('end reader')

        pass

    def get(self, url):
        return requests.get(url)


class CustomSession(BaseSession):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def __aenter__(self, *args):
        print('enter ')

        res = self.request.get(self.url)

        html = res.text
        header = res.headers

        soup = BeautifulSoup(html, 'html.parser')
        # print(soup.prettify())
        # print(header)

        return header

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print('end reader')

        pass


class AutoSession(BaseSession):

    def __init__(self, driver_path=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.chrome_path = driver_path

    async def __aenter__(self, *args):
        print('enter ')

        drivers = self.request.Chrome(self.chrome_path)

        self.request.get(self.url)

        self.request.find_element_by_xpath()



        return 'sample'

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print('end reader')
        self.request.close()


class BaseStream:

    def __init__(self, timeout=TIMEOUT, reader=None, writer=None):
        self.reader: BaseReader = reader
        self.writer: BaseWriter = writer
        self._tasks = None
        self.timeout = timeout
        self._schedule = []   # dev modifiy class type list to PrirityQueue
        print(f"{'-'*10}\nStream Info:\n{self}\n{'-'*10}")

    def __repr__(self):
        return f"STREAM :: {self.__class__} \nSET :: READER: {self.reader} \nSET :: WRITER: {self.writer}"

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

    def __init__(self, base=requests, session=BaseSession, timeout=TIMEOUT):

        if base is None:
            self.base_engine = requests
        else:
            self.base_engine = base

        if session is None:
            self.session = BaseSession
        else:
            self.session = session

        self._urls = None
        self.timeout = timeout

    def __repr__(self):
        return f"{self.__class__} :: BASE SESSION: {self.session} BASE ENGINE: {self.base_engine.__title__}"


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

            async with self.session(self.base_engine, url) as response:

                result = response

                return result


class AutoReader(BaseReader):

    def __init__(self, chrome=None, *args, **kwargs):
        super(AutoReader, self).__init__()
        self.chrome = chrome

    async def request(self, url=None):


        if issubclass(self.session, AutoSession):
            async with self.session(self.chrome, self.base_engine, url) as response:
                result = response

                return result



class BaseWriter:

    pass

