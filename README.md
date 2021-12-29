# Coroutines Web Scrapper & DB Processor


> ### What is Coroutines ?  
> - asynchronous programming
> - stable, also useful to exception handling
> 
> `Based on asyncio Stream` 

![sample](util/sample.png 'sample run img')
-----


## Feature
> - coroutines web scraper: `run_web_scrapper.py` in `test`
> - coroutines selenium scrapper : `run_selenium.py` in `test`
> - db processor: `DBConnector` in `db_connector`
> - query builder: `dev for sql query builder & http query builder`
 

-------------
## How to use


### Web Scraper (crawling)
- **run code inside `test` dir**
- when use tasks.csv
```shell
python run_web_scrapper.py --tasks path/to/tasks.csv --save_file crawling  \
                            --result_path result --result_type text
```
- when edit url list inside code, skip tasks option
```shell
python run_web_scrapper.py  --save_file crawling  \
                            --result_path result --result_type text
```

- sample run sh
```angular2html
python run_web_scrapper.py --tasks ../tasks.csv --save_file crawling  \
                            --result_path result --result_type text
```


### Selenium Scrapper

```shell
python run_selenium.py --save_file selenium  \
                            --result_path result --result_type text
```


### DB processor
- shell 'dev'
```shell
python run.py
```

## Modules
> - stream with request module: `Reader, Writer, Stream, Session` in  `stream.map`

****

## How to Custom

- ### inherit `stream.map.BaseSession`, make `CustomSession` 
- ### edit code inside async def __aenter__
- ### edit params base_session of func `asyncio_scraper` in `run_web_scrapper.py`
- ### Same as selenium scrapper
![example](util/example.png 'example')

*****

## Task lists
- [ ] selenium scrapper 
- [x] db processor code
- [x] web scrapper code
- [ ] Dev crawler using API


-------