x = set('spam')
y = {'h', 'a', 'm'}

print('dir(x) =', dir(x))

print('x =', x)
print('type(x) =', type(x))
print('y =', y)
print('x & y =', x & y)
print('x | y =', x | y)
print('x - y =', x - y)

print('{x ** 2 for x in [1, 2, 3, 4]} =', {x ** 2 for x in [1, 2, 3, 4]})
