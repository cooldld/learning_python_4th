print('class Squares, use __iter__ and __next__ to iteration')
class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop
    def __iter__(self):
        print('Squares.__iter__, self =', self)
        return self
    def __next__(self):
        print('Squares.__next__, self =', self)
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2

print()
print('for i in Squares(1, 5)')
for i in Squares(1, 5):
    print('i =', i)

print()
print('x = Squares(1, 5)')
x = Squares(1, 5)

print('''
error!!!
TypeError: 'Squares' object does not support indexing
print(x[0])
''')

print('i = iter(x)')
i = iter(x)
print('i =', i)
print('next(i) =', next(i))
print('next(i) =', next(i))
print('next(i) =', next(i))
print('next(i) =', next(i))
print('next(i) =', next(i))

print('''
error!!!
StopIteration
print('next(i) =', next(i))
''')

print('def gsquares(start, stop)')
def gsquares(start, stop):
    for i in range(start, stop + 1):
        yield i ** 2

print()
print('for i in gsquares(1, 5)')
for i in gsquares(1, 5):
    print('i =', i)
