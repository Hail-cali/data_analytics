
from stream.map import *
import time

def check_finished(task):

    if len(task) == 0:
        return True

    else:
        return False

def looger():

    pass

def asyncio_scraper(urls=None, verbose=False, test=False):

    result = []
    if not urls:

        urls = ['https://www.google.co.kr/search?q=apple', 'https://www.google.co.kr/search?q=mango',
                'https://www.google.co.kr/search?q=banana', 'https://www.google.co.kr/search?q=apple'

                 ]


    a_start = time.time()

    stream = BaseStream(reader=BaseReader(session=BaseSession))

    for l in urls:
        stream.scheduler(url=l)

    tasks = stream.executor()

    loop = asyncio.get_event_loop()

    finished, unfinished = loop.run_until_complete(
        asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED))

    for task in finished:
        result.append(task.result())


        if verbose:
            print(task.result())

    print("unfinished:", len(unfinished))

    if not check_finished(unfinished):

        finished2, unfinished2 = loop.run_until_complete(
            asyncio.wait(unfinished, timeout=2))

        for task in finished2:
            result.append(task.result())

    loop.close()

    a_end = time.time()

    print(f'asyncio {a_end - a_start:.5f}times')
    print(f'asyncio scrap done')
    print(f"{'+' * 20}")

    if test:
        b_start = time.time()
        print(f'test python normal scrap')
        for l in urls:
            f'URL: {l} || TEXT: {requests.get(l).text[100:150]}'
        b_end = time.time()

        print(f'python {b_end - b_start:.5f} times')
        print(f'python scrap done')
        print(f"{'+' * 20}")

    return result





if __name__ == '__main__':

    asyncio_scraper(url=None, verbose=False, test=True)