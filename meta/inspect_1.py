import inspect

class A:
    value = 1

    def hello(self):
        print('hello from A')

    @classmethod
    def foo(cls):
        print('this is a class method')


#print(inspect.isclass(A))
#print(inspect.getmembers(A))
#print(inspect.getmembers(A, inspect.isfunction))
print(inspect.getmembers(A, inspect.ismethod))


print(inspect.getsource(inspect.getsource))