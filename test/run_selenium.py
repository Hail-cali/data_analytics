
import os
import sys
WORKING_DIR_AND_PYTHON_PATHS = os.path.join('/', *os.getcwd().split("/")[:-1])
# print(f'before {sys.path}')
sys.path.append(WORKING_DIR_AND_PYTHON_PATHS)
# print(f'after {sys.path}')

from web_scrapper.module import asyncio_scraper
from web_scrapper.builder import BaseQueryBuilder
from stream.map import AutoSession, AutoReader

from selenium import webdriver

from opt import parse_opt
import util.logger, util.loader

OPT = parse_opt()


def main():

    link = ['https://www.google.co.kr/search?q=apple'

            ]

    # query builder for search engine like google, discode, naver
    # query_builder = BaseQueryBuilder(engine='goolge')
    # term = query_builder.build('apple -company')
    # link.append(term)

    # api for web scraper
    result = asyncio_scraper(urls=link, base_engine=webdriver, base_reader=AutoReader,
                    base_session=AutoSession, chrome=OPT.selenium_driver,
                    verbose=False, test=False)

    util.logger.save_result(OPT, *result)

if __name__ =='__main__':
    main()