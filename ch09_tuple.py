T = ()
print('dir(tuple) =', dir(T))
print('T =', T)

T = (0,)
print('T =', T)

T = (0)
print('T = (0), type(T) =', type(T))

T = (0, 1)
print('T =', T)

T = (0, 'Ni', 1.2, 3)
print('T =', T)

T = 0, 'Ni', 1.2, 3
print('T =', T)

T = ('abc', ('def', 'ghi'))
print('T =', T)

T = tuple('spam')
print('T =', T)
print('T[0] =', T[0])
print('T[-1] =', T[-1])
print('len(T) =', len(T))

T1 = (0, 'Ni', 1.2, 3)
print('T1 =', T1)
print('T + T1 =', T + T1)
print('T * 3 =', T * 3)

print('for x in T: print(x)')
for x in T: print(x)

print("'spam' in T =", 'spam' in T)
print("'p' in T =", 'p' in T)

print("T.index('p') =", T.index('p'))
print("T.index('a') =", T.index('a'))
print("T.count('p') =", T.count('p'))
print("T.count('a') =", T.count('a'))

print('list(T) =', list(T))
print('tuple(list(T)) =', tuple(list(T)))
print('sorted(T) =', sorted(T))

print('for x in T: print(x)')
for x in T: print(x)

T = (1, [2, 3], 4)
print('T =', T)
T[1][0] = 'spam'
print("T[1][0] = 'spam' --> T =", T)
