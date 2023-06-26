class A:
	pass

a = A()
b = A()
c = A()
d = A()

b.v = a
c.v = b
d.v = b

print(globals())