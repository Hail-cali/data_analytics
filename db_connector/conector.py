import pymysql
import pandas as pd
from multiprocessing import Manager
import asyncio
import key


class BaseConnector:

    ERR_MSG = {"con_err": "Connect err, check db connection",
               "get_data_err": "check command ",
               "insert_err": "insert command err",
               "col_err": "check columns name, data can't load"}


    def __init__(self, key_class):
        '''

        :param key_class: Base key instance
        '''
        if isinstance(key_class, key.base.BaseKey):
            self.db = key_class.login_db
            self.login = key_class.login
            self.login.update({'db': self.db})

        self.check_connection()

    def set_dbname(self, db):
        self.db = db
        self.login.update({'db': self.db})


    def run(self, querry):

        pass

    def check_connection(self):
        check = self.run('show tables')
        if isinstance(check, pd.DataFrame):

            print(f'\nconnected\n')
        else:
            print(self.ERR_MSG['con_err'])



class DBConnector(BaseConnector):

    def run(self, comd):

        try:
            db = pymysql.connect(**self.login)
        except:
            print(f'{self.ERR_MSG["con_err"]}')
            return
        try:
            cursor = db.cursor(pymysql.cursors.DictCursor)
            cursor.execute(comd)
        except:
            db.close(), print(f'{self.ERR_MSG["get_data_err"]}')
            return

        db.commit()
        db.close()

        result = cursor.fetchall()
        result = pd.DataFrame(result)
        return result

