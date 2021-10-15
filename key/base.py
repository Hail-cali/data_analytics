

class BaseKey:
    '''
    this is for base key structure

    '''

    def __init__(self, db='mimiciv'):

        self.login_db = db
        self.login = {"host": '',
                      'port': 8800,
                      "user": '',
                      "password": '',
                      'charset': 'utf8'}

        self.err_msg = {"con_err": "Connect err, check db connection",
                        "get_data_err": "check command ",
                        "insert_err": "insert command err"}

        self.set_login()

    def set_login(self):
        if self.login_db == 'mimiciv':
           meta = {"host": '000.00.00.000', 'port': 8800, "user": 'sample', "password": 'sample', 'charset': 'utf8'}

        else:
            meta = dict()
            print('check meta table')

        self.login.update(meta)