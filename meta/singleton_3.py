#-*-coding:utf-8-*-


class SingletonMeta(type):
    def __call__(cls, *args, **kwargs):
        print(f'singletonMeta {cls}')
        if hasattr(cls, '_ins'):
            return cls._ins
        else:
            ins = super().__call__(*args, **kwargs)
            setattr(cls, '_ins', ins)
            return ins


class A(metaclass = SingletonMeta):
    def __init__(self):
        print('init new A')
        self.name = 'a'

# 改变行为
a = A()
b = A()

b.name = 'b'

print(a is b)
print(a.name)

