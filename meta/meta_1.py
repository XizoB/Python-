#-*-coding:utf-8-*-

class NormalClass:
	FLAG = 1

	def __init__(self, name):
		self.name = name

	def hello(self):
		print(f"NormalClass, name={self.name}, flag={self.FLAG}")




c = NormalClass('abc')
c.hello()

def method_init(self, name):
	self.name = name

def method_hello(self):
	print(f"NormalClass, name={self.name}, flag={self.FLAG}")


	
d = DynamicClass('xxx')
d.hello()
