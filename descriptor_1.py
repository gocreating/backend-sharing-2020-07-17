class Obj():
    foo = 'class foo'

    def __init__(self):
        self.foo = 'instance foo'

obj = Obj()

print(obj.foo)
