#this is test file


from db_connector.conector import DBConnector
import key.private

def test():
    my_key = key.private.SecretKey(preset_db='mimiciv')


    com = DBConnector(my_key)
    print(com.login)
    pass

if __name__ == '__main__':
    test()

