#-*- coding:utf-8 -*-

class ThisIsADescriptor:
    def __set_name__(self, owner, name):
        print(f'descriptor.__set_name__ is called. owner={owner}, name={name}')
        self.public_name = name
        self.private_name = '_' + name

    # 为什么使用的是private_name
    def __get__(self, obj, objtype=None):
        print(f'descriptor.__get__ is called. self={self}, obj={obj}, objtype={objtype}')
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        print(f'descriptor.__set__ is called. self={self}, obj={obj}, value={value}')
        setattr(obj, self.private_name, value)

class A:
    prop = ThisIsADescriptor()

a = A()
a.prop = 'abc'

print(a.prop)
