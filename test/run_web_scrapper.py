
import os
import sys
WORKING_DIR_AND_PYTHON_PATHS = os.path.join('/', *os.getcwd().split("/")[:-1])
# print(f'before {sys.path}')
sys.path.append(WORKING_DIR_AND_PYTHON_PATHS)
# print(f'after {sys.path}')

from web_scrapper.module import asyncio_scraper


OPT = ''

def main():

    wrong_link = ['https://www.google.co.kr/search?q=apple', 'https://www.google.co.kr/search?q=mango',
                 'https://www.google.co.kr/search?q=banana', 'https://www.google.co.kr/search?q=apple',
                'https://www.google.co.kr/search?q=kiwi', 'https://www.google.co.kr/search?q=dev',
                 'wrong:link']

    link = ['https://www.google.co.kr/search?q=apple', 'https://www.google.co.kr/search?q=mango',
            'https://www.google.co.kr/search?q=banana', 'https://www.google.co.kr/search?q=apple'
            'https://www.google.co.kr/search?q=kiwi', 'https://www.google.co.kr/search?q=dev',
            'https://www.google.co.kr/search?q=python', 'https://www.google.co.kr/search?q=asycnio',
            ]

    asyncio_scraper(urls=link, verbose=False, test=False)


if __name__ =='__main__':
    main()