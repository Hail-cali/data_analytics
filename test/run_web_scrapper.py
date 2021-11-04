
import os
import sys
WORKING_DIR_AND_PYTHON_PATHS = os.path.join('/', *os.getcwd().split("/")[:-1])
# print(f'before {sys.path}')
sys.path.append(WORKING_DIR_AND_PYTHON_PATHS)
# print(f'after {sys.path}')

from web_scrapper.module import asyncio_scraper
from web_scrapper.builder import BaseQueryBuilder

OPT = ''

def main():

    wrong_link = ['https://www.google.co.kr/search?q=apple', 'https://www.google.co.kr/search?q=mango',
                 'https://www.google.co.kr/search?q=banana', 'https://www.google.co.kr/search?q=apple',
                'https://www.google.co.kr/search?q=kiwi', 'https://www.google.co.kr/search?q=dev',
                 'wrong:link']

    link = ['https://www.google.co.kr/search?q=apple', 'https://www.google.co.kr/search?q=mango',
            'https://www.google.co.kr/search?q=banana', 'https://www.google.co.kr/search?q=numpy',
            'https://www.google.co.kr/search?q=kiwi', 'https://www.google.co.kr/search?q=apple',
            'https://www.google.co.kr/search?q=python', 'https://www.google.co.kr/search?q=asycnio',
            ]

    query_builder = BaseQueryBuilder(engine='goolge')
    term = query_builder.build('apple')

    link.append(term)
    asyncio_scraper(urls=link, verbose=False, test=True)


if __name__ =='__main__':
    main()