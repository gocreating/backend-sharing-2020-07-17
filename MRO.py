class A():
    def show(self):
        print('a.show')

class B(A):
    pass

class C(A):
    def show(self):
        print('c.show')

class D(B, C):
    pass

print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

D().show()
# c.show
