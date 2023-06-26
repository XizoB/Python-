import objgraph  #pip3 install objgraph
import gc


class A(object):
	pass

a = A()
b = A()
c = A()

a.v = b
#c.v = a



objgraph.show_refs([a], filename='refs.png')
objgraph.show_backrefs([a], filename='backrefs.png')

