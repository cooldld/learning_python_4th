print('class Indexer, use __getitem__() to index')
class Indexer:
    def __getitem__(self, index):
        return index ** 2

print()
print('x = Indexer()')
x = Indexer()

print('x[3] =', x[3])

'''
error!!!
TypeError: 'Indexer' object does not support item assignment
x[3] = 1
'''

print()
print('for i in range(5)')
for i in range(5):
    print('x[%s] = %s' % (i, x[i]))

print()
print('class Indexer, use __getitem__() and __setitem__() to slice')
class Indexer:
    data = [5, 6, 7, 8, 9]
    def __getitem__(self, index):
        print('Indexer.__getitem__, index =', index)
        return self.data[index]
    def __setitem__(self, index, value):
        self.data[index] = value

print()
print('x = Indexer()')
x = Indexer()
print('x.data =', x.data)

print()
print('for i in range(5)')
for i in range(5):
    print('x[%s] = %s' % (i, x[i]))

print('x[-1] =', x[-1])
print('x[2:4] =', x[2:4])
print('x[1:] =', x[1:])
print('x[:-1] =', x[:-1])
print('x[::2] =', x[::2])

print()
print('x.data =', x.data)
print('x[3] = 1')
x[3] = 1
print('x.data =', x.data)
