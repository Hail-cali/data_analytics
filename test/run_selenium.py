
import os
import sys
WORKING_DIR_AND_PYTHON_PATHS = os.path.join('/', *os.getcwd().split("/")[:-1])
# print(f'before {sys.path}')
sys.path.append(WORKING_DIR_AND_PYTHON_PATHS)
# print(f'after {sys.path}')

from web_scrapper.module import asyncio_scraper
from web_scrapper.builder import BaseQueryBuilder

import requests
from stream.map import AutoSession


from selenium import webdriver


OPT = ''

def main():



    link = ['https://www.google.co.kr/search?q=apple', 'https://www.google.co.kr/search?q=mango',
            'https://www.google.co.kr/search?q=banana', 'https://www.google.co.kr/search?q=numpy',
            ]

    # query builder for search engine like google, discode, naver
    # query_builder = BaseQueryBuilder(engine='goolge')
    # term = query_builder.build('apple -company')
    # link.append(term)

    chrome_path = '/Users/george/PycharmProjects/TextMining_study/selenium_server/chromedriver_linux64_83'
    drivers = webdriver.Chrome(chrome_path)
    # api for web scraper
    asyncio_scraper(urls=link, base_engine=drivers,
                    base_session=AutoSession,
                    verbose=False, test=False)


if __name__ =='__main__':
    main()