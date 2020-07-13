class DataDescriptor():
    # Rule 1: The result of the __get__ method of the data descriptor of the same name attached to the class if it exists
    def __get__(self, obj, type):
        return '__get__'

    def __set__(self, obj, value):
        print('__set__')

class NonDataDescriptor():
    # Rule 1: The result of the __get__ method of the data descriptor of the same name attached to the class if it exists
    def __get__(self, obj, type):
        return '__get__'

# Rule 5: repeating for each type in the mro until it finds a match
class ObjParent():
    def __init__(self):
        pass

class Obj(ObjParent):
    # Rule 4: or else it falls back to look in the type(obj).__dict__
    foo = 'Obj.foo'
    foo = NonDataDescriptor()

    def __init__(self):
        # Rule 2: Or the corresponding value in obj.__dict__ if it exists
        # self.foo = 'obj.foo'
        pass


obj = Obj()

print(obj.foo)
