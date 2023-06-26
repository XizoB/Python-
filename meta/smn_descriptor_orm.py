class Field:

    def __set_name__(self, owner, name):
        self.fetch = f'SELECT {name} FROM {owner.table} WHERE {owner.key}=?;'
        self.store = f'UPDATE {owner.table} SET {name}=? WHERE {owner.key}=?;'

    def __get__(self, obj, objtype=None):
        #return conn.execute(self.fetch, [obj.key]).fetchone()[0]
        return f'execute:{self.fetch}, [{obj.key}]'

    def __set__(self, obj, value):
        #conn.execute(self.store, [value, obj.key])
        #conn.commit()
        print(f'execute:{self.store} [{value}, {obj.key}]')

class Movie:
    table = 'Movies'                    # Table name
    key = 'title'                       # Primary key
    director = Field()
    year = Field()

    def __init__(self, key):
        self.key = key

m = Movie('title')
print(m.year)
m.year = 100