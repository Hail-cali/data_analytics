import pymysql
import pandas as pd
from multiprocessing import Manager

class DBsysyem(object):

    ERR_MSG = {"con_err": "Connect err, check db connection",
               "get_data_err": "check command ",
               "insert_err": "insert command err"}

    def __init__(self, login, db_name='db_name'):
        self.db = db_name
        self.login = login
        self.login.update({'db': self.db})

    def set_dbname(self, db):
        self.db = db
        self.login.update({'db': self.db})

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

    # @Manager
    # def multi_run(self):