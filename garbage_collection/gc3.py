class A:
	pass

a = A()
b = A()
c = A()

a.v = b
b.v = c
c.v = a