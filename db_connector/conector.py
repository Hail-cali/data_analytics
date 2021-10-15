import pymysql
import pandas as pd
from multiprocessing import Manager
import asyncio



class BaseConnector:


    ERR_MSG = {"con_err": "Connect err, check db connection",
               "get_data_err": "check command ",
               "insert_err": "insert command err",
               "col_err": "check columns name, data can't load"}


    def __init__(self, login, db_name='db_name'):
        self.db = db_name
        self.login = login
        self.login.update({'db': self.db})
        self.check_connection()

    def set_dbname(self, db):
        self.db = db
        self.login.update({'db': self.db})


    def run(self, querry):

        pass

    def check_connection(self):

        if isinstance(self.run('show tables'), object):
            print(f'\nconnected\n')
        else:
            print(self.ERR_MSG['con_err'])



