print('class stepper, use __getitem__() to iterate')
class stepper:
    def __getitem__(self, i):
        return self.data[i]

print()
print('x = stepper()')
x = stepper()
print("x.data = 'spam'")
x.data = 'spam'

print()
print('for item in x')
for item in x:
    print('item =', item)

print()
print("'p' in x =", 'p' in x)

print('[c for c in x] =', [c for c in x])

print('list(map(str.upper, x)) =', list(map(str.upper, x)))

print('(a, b, c, d) = x')
(a, b, c, d) = x
print('a = %s, b = %s, c = %s, d = %s' % (a, b, c, d))
