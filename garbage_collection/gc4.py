import gc
class A(object):
	pass

a = A()
b = A()
c = A()

a.v = b
b.v = c
c.v = a
a.__dict__
b.__dict__
c.__dict__

del a
del b
del c

gc.set_debug(gc.DEBUG_SAVEALL)

gc.enable()
print(gc.collect())

print(gc.garbage)
