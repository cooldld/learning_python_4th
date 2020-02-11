L = [4, 5, 6]

X = L * 2
Y = [L] * 2

print('L =', L)
print('X, L * 2 =', X)
print('Y, [L] * 2 =', Y)

L[1] = 0
print('L[1] = 0')
print('X =', X)
print('Y =', Y)
