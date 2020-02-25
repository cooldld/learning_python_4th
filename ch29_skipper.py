s = 'abc'

print('s =', s)

print()
print('字符串s有两个独立的迭代器对象x和y')
print('for x in s')
print('for y in s')
print('x + y =')
for x in s:
    for y in s:
        print(x + y, end = ' ')
print()

print()
print('class Skip_iterator')
class Skip_iterator:
    def __init__(self, wrapped):
        #print('Skip_iterator, init, wrapped =', wrapped)
        self.wrapped = wrapped #wrapped is iterator state information
        self.offset = 0
    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 1
            return item

print()
print('class Skip_object')
class Skip_object:
    def __init__(self, wrapped):
        #print('Skip_object, init, wrapped =', wrapped)
        self.wrapped = wrapped
    def __iter__(self):
        return Skip_iterator(self.wrapped)

if __name__ == '__main__':
    print('\nself test')
    alpha = 'abc'
    print('alpha =', alpha)
    print('skipper = Skip_object(alpha)')
    skipper = Skip_object(alpha)
    print('I1 = iter(skipper)')
    I1 = iter(skipper)
    print('I2 = iter(skipper)')
    I2 = iter(skipper)
    print('next(I1) =', next(I1))
    print('next(I2) =', next(I2))
    print('next(I1) =', next(I1))
    print('next(I1) =', next(I1))
    print('next(I2) =', next(I2))
    print('next(I2) =', next(I2))

    print()
    print('for x in skipper')
    print('for y in skipper')
    print('x + y =')
    for x in skipper:
        for y in skipper:
            print(x + y, end = ' ')
    print()
