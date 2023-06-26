#-*- coding:utf-8 -*-

class A:

    #NOTE 无穷递归， 效率问题
    def __getattribute__(self, name):
        print(f'__getattribute__ {name} is called')
        return super().__getattribute__(name)

    # lazy init
    def __getattr__(self, name):
        print(f'__getattr__ {name} is called')
        v = 'dave' # for some resources
        setattr(self, name, v)
        return v

a = A()
print(f'name is {a.name}')
print(f'name is {a.name}')

