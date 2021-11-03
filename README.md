# DB Processor & Web scraper (Fast & Stable)

## Based on asyncio Stream, Multi processing


## feature
- db connector: `DBConnector` in `db_connector`
- stream with request module: `Reader, Writer, Stream, Session` in  `stream.map` 
- fast & stable web scraper: `module` in `web_scrapper`
- query builder: `dev for sql query builder & http query builder` 

-------------
## how to use
### DB processor
- shell 'dev'
```shell
python run.py
```

### web scraper
- shell
```shell
python run_web_scrapper.py -l https://google.com https://google.com 
```
or simply edit in run file (add url list)
```shell
python run_web_scrapper.py  
```
