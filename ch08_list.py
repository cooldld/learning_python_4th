#create a list
L = []
print('L =', L)

L = [0, 1, 2, 3]
print('L =', L)

L = ['abc', ['def', 'ghi']]
print('L =', L)

L = list('spam')
print('L =', L)

L = list(range(-4, 4))
print('L =', L)

print('L[0] =', L[0])
print('L[0:3] =', L[0:3])
print('len(L) =', len(L))

L1 = L
print('L1 =', L1)
L2 = list('spam')
print('L2 =', L2)

print('L1 + L2 =', L1 + L2)
print('L2 * 3 =', L2 * 3)
print('for x in L2: print(x) =')
for x in L2: print(x)

print('3 in L1 =', 3 in L1)

L2.append(4)
print('L2.append(4) =', L2)

L2.extend([5, 6, 7])
print('L2.extend([5, 6, 7]) =', L2)

L2.insert(0, 8)
print('L2.insert(0, 8) =', L2)

print('L2.index(8) =', L2.index(8))
print("L2.index('s') =", L2.index('s'))

print("L2.count('s') =", L2.count('s'))

L1.sort()
print('L1.sort() =', L1)
L1.reverse()
print('L1.reverse() =', L1)

del L2[0]
print('del L2[0] =', L2)
del L2[4:]
print('del L2[4:] =', L2)

print('L2.pop() =', L2.pop())
print('L2 =', L2)

L2.remove('p')
print("L2.remove('p') =", L2)

L1[3:-1] = []
print('L1[3:-1] = [], =', L1)

L1[3:-1] = [8, 11, 34]
print('L1[3:-1] = [8, 11, 34], =', L1)

L3 = [x ** 2 for x in range(5)]
print('L3 =', L3)

L3 = list(map(ord, 'spam'))
print('L3 =', L3)

L1 = ['abc', 'ABC', 'aBe']
print('L1 =', L1)
L1.sort()
print('L1.sort() =', L1)
L1 = ['abc', 'ABC', 'aBe']
L1.sort(key = str.lower)
print('L1.sort(key = str.lower) =', L1)
L1 = ['abc', 'ABC', 'aBe']
L1.sort(key = str.lower, reverse = True)
print('L1.sort(key = str.lower, reverse = True) =', L1)
