print('class Iters, def __getitem__/__iter__/__next__/__contains__')
class Iters:
    def __init__(self, value):
        self.data = value
    def __getitem__(self, i):
        print('call __getitem__, i =', i)
        return self.data[i]
    def __iter__(self):
        print('call __iter__')
        self.ix = 0
        return self
    def __next__(self):
        print('call __next__')
        if self.ix == len(self.data): raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item
    def __contains__(self, x):
        print('call __contains__, x =', x)
        return x in self.data

print()
print('x = Iters([1, 2, 3, 4, 5])')
x = Iters([1, 2, 3, 4, 5])

print()
print('3 in x')
print(3 in x)

print()
print('for i in x')
for i in x:
    print('i =', i)

print()
print('i = iter(x)')
i = iter(x)
while True:
    try:
        print('next(i) =', next(i))
    except StopIteration:
        break

print()
print('[i ** 2 for i in x]')
print([i ** 2 for i in x])

print()
print('list(map(bin, x))')
print(list(map(bin, x)))

print()
print("x = Iters('spam')")
x = Iters('spam')
print('x[0] =', x[0])
print('x[1:] =', x[1:])
print('x[:-1] =', x[:-1])
