#https google query builder

class BaseQueryBuilder:

    def __init__(self, engine='google'):
        self._engine: str = engine
        self.url = f"https://www.google.co.kr/search?q="
        self._term = f''


    def __repr__(self):
        return f'__Web_class__QueryBuilder_search_engine:{self.engine}'

    def build(self, *args):
        for t in args:
            self.term += f' {t}'
        return f'{self.url}{self.term}'

    @property
    def engine(self):
        return self._engine

    @property
    def term(self):
        return self._term

    @engine.setter
    def engine(self, search_engine):
        if search_engine == 'google':
            self._engine = 'google'

    @term.setter
    def term(self, terms):
        self._term = terms



if __name__ == '__main__':
    builder = BaseQueryBuilder(engine='google')
    print(builder)
    print(builder.build('hello', 'here'))