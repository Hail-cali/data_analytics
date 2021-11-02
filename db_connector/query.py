from collections.abc import Iterable

class BaseBuilder:

    def __init__(self, cls=None):
        self.cls = cls
        self._query = []


    def check_validation(self, *args):
        '''
        need some rule for  check validation
        :return: Bool
        '''
        return True

    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, *args):

        for arg in args[0]:
            self._query.append(arg)


    def _end(self):
        self.query = ';'

    def flush(self):
        print(f'flushed ')

        result = f''
        for _ in range(len(self.query)):
            result += self.query.pop(0)
        return result

    def make(self):
        self._end()
        return self.flush()




class Sql(BaseBuilder):

    def __init__(self, *args):
        super().__init__(*args)
        self._col = f''
        self._from = f' FROM'
        self._where = f' WHERE'

    @property
    def columns(self):
        return self._col

    @property
    def columns(self, *args):
        self._col += args[0]

    @property
    def FROM(self):
        return self._from

    @FROM.setter
    def FROM(self, table):

        if self.check_validation(table):
            self._from += f' {table}'

    @property
    def where(self):
        return self._where

    @where.setter
    def where(self, *args):
        self._where = f' WHERE'

        if isinstance(args[0], str):
            self._where += f' {args[0]}'

        else:
            for d in args[0]:
                print(d)
                self._where += f' {d}'

    def make(self):

        self.query = self.FROM, self.where

        self._end()
        return self.flush()


if __name__ == '__main__':

    sql = Sql()
    sql.where = 'hire', 'here'
    sql.FROM = 'table'

    query = sql.make()
    print(query)

    print()
