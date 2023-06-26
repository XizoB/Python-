#-*-coding:utf-8-*-
import random

class Meta(type):
	def __new__(cls, name, bases, dct):
		# name = 'NormalClass
		# bases = ()
		# dct = {'FLAG', __init__ , }
		print(cls, name, bases, dct)
		dct['FLAG'] = 3
		#dct.pop('hello', None)
		
		return super().__new__(cls, name, bases, dct)


class NormalClass(metaclass=Meta):
	FLAG = 1

	def __init__(self, name):
		self.name = name

	def hello(self):
		print(f"NormalClass, name={self.name}, flag={self.FLAG}")

d = NormalClass('abc')
d.hello()