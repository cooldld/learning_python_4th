print('class c_wrapper, def __getattr__')
class c_wrapper:
    def __init__(self, object):
        self.wrapped = object
    def __getattr__(self, attrname):
        print('c_wrapper.__getattr__, trace attrname =', attrname)
        return getattr(self.wrapped, attrname)

print()
print('x = c_wrapper([1, 2, 3])')
x = c_wrapper([1, 2, 3])
print('x.wrapped =', x.wrapped)
print('x.append(4)')
x.append(4)
print('x.wrapped =', x.wrapped)

print()
print("x = c_wrapper({'a': 1, 'b': 2})")
x = c_wrapper({'a': 1, 'b': 2})
print('x.wrapped =', x.wrapped)
print('x.keys() =', x.keys())
