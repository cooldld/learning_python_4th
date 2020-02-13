L1 = [1, 2, 3, 4]
#L2 = [10, 20, 30, 40]
L2 = ['a', 'b', 'c', 'd']
#L2 = ['b', 'c', 'd']

print('L1 =', L1)
print('L2 =', L2)
print('zip(L1, L2) =', zip(L1, L2))
print('list(zip(L1, L2)) =', list(zip(L1, L2)))

print('for (x, y) in zip(L1, L2)')
for (x, y) in zip(L1, L2):
    print('x = %s, y= %s' % (x, y))
