class IntValidator:
    def __init__(self, default, minint, maxint):
        self.minint = minint
        self.maxint = maxint
        self.default = default

    def __set_name__(self, owner, name):
        # print(f'descriptor.__set_name__ is called. owner={owner}, name={name}')
        self.public_name = name
        self.private_name = '_' + name

    # 为什么使用的是private_name
    def __get__(self, obj, objtype=None):
        # print(f'descriptor.__get__ is called. self={self}, obj={obj}, objtype={objtype}')
        if not hasattr(obj, self.private_name):
            setattr(obj, self.private_name, self.default)

        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        # print(f'descriptor.__set__ is called. self={self}, obj={obj}, value={value}')
        if value >= self.minint and value <= self.maxint:
            setattr(obj, self.private_name, value)
        else:
            raise RuntimeError()


class A:
    age = IntValidator(0, 0, 200)

a = A()
print(f'default age: {a.age}')

a.age = 25
print(f'cur age: {a.age}')

a.age = 210