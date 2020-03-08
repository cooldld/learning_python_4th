print('def decorator(cls)')
def decorator(cls):
    class c_wrapper:
        def __init__(self, *args):
            print('c_wrapper.__init__')
            self.wrapper = cls(*args)
        def __getattr__(self, name):
            print('c_wrapper.__getattr__')
            return getattr(self.wrapper, name)
    return c_wrapper

print()
print('@decorator')
print('class c_c')
@decorator
class c_c:
    def __init__(self, x, y):
        print('c_c, __init__')
        self.attr = 'spam'

print()
print('x = c_c(6, 7)')
x = c_c(6, 7)
print('x =', x)

print()
print('x.attr =')
print(x.attr)

