print('class Commuter, def __add__/__radd__')
class Commuter:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        print('__add__, val = %s, other = %s' % (self.val, other))
        return self.val + other
    def __radd__(self, other):
        print('__radd__, val = %s, other = %s' % (self.val, other))
        return other + self.val

print()
print('x = Commuter(1)')
x = Commuter(1)
print('y = Commuter(100)')
y = Commuter(100)

print('x + 1')
print(x + 1)

print('1 + y')
print(1 + y)

print('x + y')
print(x + y)

print()
print('class Commuter, def __add__/__radd__, improved')
class Commuter:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        print('__add__, val = %s, other = %s' % (self.val, other))
        if isinstance(other, Commuter): other = other.val
        return Commuter(self.val + other)
    def __radd__(self, other):
        print('__radd__, val = %s, other = %s' % (self.val, other))
        return Commuter(other + self.val)
    def __repr__(self):
        print('__repr__, val =', self.val)
        return 'Commuter, val = %s' % self.val

print()
print('x = Commuter(1)')
x = Commuter(1)
print('y = Commuter(100)')
y = Commuter(100)

print('z = x + 1')
z = x + 1
print('z =', z)

print('z = 1 + y')
z = 1 + y
print('z =', z)

print('z = x + y')
z = x + y
print('z =', z)
