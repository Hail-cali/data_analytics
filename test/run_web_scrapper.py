
import os
import sys
WORKING_DIR_AND_PYTHON_PATHS = os.path.join('/', *os.getcwd().split("/")[:-1])
# print(f'before {sys.path}')
sys.path.append(WORKING_DIR_AND_PYTHON_PATHS)
# print(f'after {sys.path}')

from web_scrapper.module import asyncio_scraper
from web_scrapper.builder import BaseQueryBuilder

import requests
from stream.map import CustomSession

from opt import parse_opt
import util.logger, util.loader
OPT = parse_opt()

def main():

    wrong_link = ['wrong:link','https://www.google.co.kr/search?q=apple', 'https://www.google.co.kr/search?q=mango',
                 'https://www.google.co.kr/search?q=banana', 'https://www.google.co.kr/search?q=apple',
                'https://www.google.co.kr/search?q=kiwi', 'https://www.google.co.kr/search?q=dev',
                 'wrong:link']

    link = ['https://www.google.co.kr/search?q=apple', 'https://www.google.co.kr/search?q=mango',
            'https://www.google.co.kr/search?q=banana', 'https://www.google.co.kr/search?q=numpy',
            'https://www.google.co.kr/search?q=kiwi', 'https://www.google.co.kr/search?q=apple',
            'https://www.google.co.kr/search?q=python', 'https://www.google.co.kr/search?q=asycnio',
            ]

    if OPT.tasks:
        file = util.loader.load_csv(OPT.tasks)
        link = [link[0] for link in file]
        print(link)
    # query builder for search engine like google, discode, naver
    # query_builder = BaseQueryBuilder(engine='goolge')
    # term = query_builder.build('apple -company')
    #
    # link.append(term)

    # api for web scraper
    result = asyncio_scraper(urls=link, base_engine=requests,
                    base_session=CustomSession,
                    verbose=False, test=False)

    util.logger.save_result(OPT, *result)

if __name__ =='__main__':
    main()