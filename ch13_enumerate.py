s = 'spam'
print('s =', s)
print('enumerate(s) =', enumerate(s))
print('for (offset, item) in enumerate(s)')
for (offset, item) in enumerate(s):
    print('offset = %s, item = %s' % (offset, item))

L = ['a', 'b', 'c', 'd']
print('L =', L)
E = enumerate(L)
print('enumerate(L) =', E)
print('next(E) =', next(E))
print('next(E) =', next(E))
print('next(E) =', next(E))
print('next(E) =', next(E))
print('for (offset, item) in enumerate(L)')
for (offset, item) in enumerate(L):
    print('offset = %s, item = %s' % (offset, item))
