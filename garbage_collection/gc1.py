#-*-coding:utf-8-*-

import sys

class A:
	pass

a = A()

# 1 more, because getrefcount alse has a reference to the object when called.
print(sys.getrefcount(a))


b = A()
b.v = a
print(f'after referenced by b, refcount is:{sys.getrefcount(a)}')

del b.v
print(f'after del attribute of b, refcount is:{sys.getrefcount(a)}')

b.v = a
del b
print(f'after del object b, refcount is:{sys.getrefcount(a)}')


