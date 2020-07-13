class LazyProperty(object):
    def __init__(self, func):
        self._func = func
        self.__name__ = func.__name__
    def __get__(self, obj, klass):
        print('Called the func')
        result = self._func(obj)
        obj.__dict__[self.__name__] = result
        return result

class MyClass(object):
    @LazyProperty
    def x(self):
        return 42


obj = MyClass()
print(obj.x)
print(obj.x)
