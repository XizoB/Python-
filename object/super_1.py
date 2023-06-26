class A:
    def hi(self):
        print('A')

class B(A):
    def hi(self):
        print('B')

class C(B):
    def hi(self):
        print('C')

class D(C):
    def hi(self):
        print('D')

d = D()
print(D.__mro__)
# d.hi()

super(D, d).hi()

