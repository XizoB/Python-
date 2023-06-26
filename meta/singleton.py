
class A:
	_ins = None

	def __init__(self):
		print('create new instance')

	
	@classmethod
	def get(cls):
		if cls._ins is None:
			cls._ins = cls()
		
		return cls._ins

a = A.get()
b = A.get()

print(a is b)

c = A()
print(a is c)