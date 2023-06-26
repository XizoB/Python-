#-*-coding:utf-8-*-


class SingletonMeta(type):
	def __new__(cls, name, bases, dct):
		
		#SingletonMeta(metaclass) -> newcls(class, A)  -> instance
		newcls = super().__new__(cls, name, bases, dct)
		
		ins = newcls()
		newcls.__single_instance__ = ins

		def singleton_new(ncls, *args, **kwargs):
			print('singleton new, use cached one.')
			return ncls.__single_instance__
		
		def singleton_init(self, *args, **kwargs):
			pass

		# newcls.__new__ = singleton_new
		setattr(newcls, '__new__', singleton_new)

		# 尝试不设置__init__会发生什么事情
		setattr(newcls, '__init__', singleton_init)
		return newcls
	
	def __init__(self, name, bases, dic):
		print('SingletonMeta.__init__')
		super().__init__(name, bases, dic)
		return


class A(metaclass = SingletonMeta):
	def __init__(self):
		print('init new A')
		self.name = 'a'


print('==================')

a = A()
b = A()

b.name = 'b'
c = A()

print(a is b)
print(a.name)