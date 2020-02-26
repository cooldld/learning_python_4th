print('class Life, def __del__')
class Life:
    def __init__(self, name='unknown'):
        print('__init__, hello, name =', name)
        self.name = name
    def __del__(self):
        print('__del__, goodbye, name =', self.name)

print()
print("x = Life('manba')")
x = Life('manba')
print('x =', x)
print('x.name =', x.name)

print()
print('y = x')
y = x
print('y =', y)
print('y.name =', y.name)

print()
print("x = 'nihao'")
x = 'nihao'

print()
print('y =', y)
print('y.name =', y.name)

