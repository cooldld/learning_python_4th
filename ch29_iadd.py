print('class Number, def __iadd__')
class Number:
    def __init__(self, val):
        self.val = val
    def __iadd__(self, other):
        print('__iadd__, val = %s, other = %s' % (self.val, other))
        self.val += other
        return self

print()
print('x = Number(5)')
x = Number(5)
print('x += 1')
x += 1
print('x += 1')
x += 1
print('x.val =', x.val)

print()
print('class Number, def __add__')
class Number:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        print('__add__, val = %s, other = %s' % (self.val, other))
        return Number(self.val + other)

print()
print('x = Number(15)')
x = Number(15)
print('x += 1')
x += 1
print('x += 1')
x += 1
print('x.val =', x.val)
