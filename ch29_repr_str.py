print('class adder, def __add__')
class adder:
    def __init__(self, value = 0):
        self.data = value
    def __add__(self, other):
        self.data += other

print()
print('x = adder()')
x = adder()
print('x =', x)

print()
print('class addrepr(adder), def __repr__')
class addrepr(adder):
    def __repr__(self):
        print('call __repr__')
        return 'addrepr, data = %s' % self.data

print()
print('x = addrepr()')
x = addrepr()
print('x =', x)
print('x + 1')
x + 1
print('x =', x)

print('x + 10')
x + 10
print('x =', x)

print()
print('repr(x) =', repr(x))
print('str(x) =', str(x))

print()
print('class addboth(adder), def __str__/__repr__')
class addboth(adder):
    def __str__(self):
        print('call __str__')
        return 'addboth, data = %s' % self.data
    def __repr__(self):
        print('call __repr__')
        return 'addboth, data = %s' % self.data

print()
print('x = addboth()')
x = addboth()
print('x =', x)
print('x + 1')
x + 1
print('x =', x)
