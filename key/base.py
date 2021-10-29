

class BaseKey:
    '''
    this is for base key structure
    '''

    def __init__(self, preset_db=None):

        self._login_db = preset_db
        self._login = {"host": '',
                      'port': 8800,
                      "user": '',
                      "password": '',
                      'charset': 'utf8'}

        self.preset_login()

    @property
    def login(self, **kwargs):

        self._login.update(kwargs)

    @property
    def login_db(self, new):
        self._login_db = new

    @login.getter
    def login(self):
        return self._login

    @login_db.getter
    def login_db(self):
        return self._login_db

    def preset_login(self):
        '''
        :set: set database info in login like self.login.update({host:00})
        need  to override base class, fill preset_login method
        :return: None
        '''
        pass

class SampleKey(BaseKey):

    '''
    this class is sample key classs for set login info
    '''
    def preset_login(self):
        if self.login_db == 'sample':
            meta = {"host": '192.168.1.1', 'port': 8000, "user": 'user', "password": 'passwd',
                    'charset': 'utf8'}

        self.login.update(meta)