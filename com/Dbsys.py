import pymysql
import pandas as pd
from multiprocessing import Manager

class DBsysyem(object):

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

    def make_query(self, *args, purpose='items', how='left', on='', hr=(0,48)):
        query_list = []

        for q_set in args:

            cols = self.isintable(q_set[0], q_set[1])
            #print(cols)
            query_header = query_col = query_join = query_where = str()

            if purpose == 'items':
                query_header = f'select distinct mic.stay_id, ih.hr, '
                query_col = [f'{q_set[0]}.{c}' for c in q_set[1]]
                query_join = f'''
                        from {q_set[0]}
                        left join mimiciv.icustays mic on {q_set[0]}.hadm_id =  mic.hadm_id
                        inner join icustay_hourly_co ih on mic.stay_id = ih.stay_id
                        '''
                query_where = f'where ih.hr between {hr[0]} and {hr[1]} and {q_set[0]}.charttime between ih.starttime and ih.endtime'

                query = query_header + ', '.join(query_col) + query_join + query_where
                query_list.append(query)

            elif purpose == 'frame':
                query_header = f'select distinct {q_set[0]}.stay_id, {q_set[0]}.hr, '
                query_col = f'mic.first_careunit '
                query_join = f'from {q_set[0]} left join mimiciv.icustays mic on mic.stay_id = {q_set[0]}.stay_id '
                query_where = f'where {q_set[0]}.hr between {hr[0]} and {hr[1]} '

                query = query_header + query_col + query_join + query_where
                query_list.append(query)

        return query_list

    def isintable(self, table, cols):
        in_col = self.run(f'show columns from {table}')

        if not self.multi_search_filed(cols, in_col):
            print(self.ERR_MSG['col_err'])
            return

        return in_col.Field

    def multi_search_filed(self, com_col, in_col):

        '''
        :param com_col: commnad columns
        :param in_col: existed columns in table
        :return: bool
        '''
        return True

    def match_table_col(self, table, columns=[]):

        return (table, columns)

    def match_dict(self, **kwargs):
        result = []

    def check_connection(self):

        if isinstance(self.run('show tables'),object):
            print(f'\nconnected\n')
        else:
            print(self.ERR_MSG['con_err'])

class DBsystem(DBsysyem):

    def __init__(self):
        super().__init__()
        self.x = None

    def convert(self, X):

        pass
