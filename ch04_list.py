L = [123, 'spam', 1.23]

print('dir(L) =', dir(L))
print('L =', L)
print('len(L) =', len(L))
print('L[0] =', L[0])
print('L[:-1] =', L[:-1])
print('L + [4, 5, 6] =', L + [4, 5, 6])

L.append('NI')
print('L.append NI =', L)

print('L.pop(2) =', L.pop(2))
print('L =', L)

L = ['bb', 'aa', 'cc']
print('L =', L)
L.sort()
print('L.sort() =', L)
L.reverse()
print('L.reverse() =', L)

M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('M =', M)
print('M[1] =', M[1])
print('M[1][2] =', M[1][2])

col2 = [row[1] for row in M]
print('col2 =', col2)

col3 = [row[1] for row in M if row[1] % 2 == 0]
print('col3 =', col3)

col4 = [M[i][i] for i in [0, 1, 2]]
print('col4 =', col4)

col5 = [c * 2 for c in 'spam']
print('col5 =', col5)
