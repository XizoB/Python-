class GameObject:
    def hi(self):
        pass

class A:
    def hi(self):
        
        print('A')

class B(A):
    def hi(self):
        super().hi()
        print('B')

class C(B):
    def hi(self):
        super().hi()
        print('C')

class D(C):
    def hi(self):
        super().hi()
        print('D')

d = D()
print(D.__mro__)
d.hi()


