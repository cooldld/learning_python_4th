print("S = 'spam'")
S = 'spam'

print("B = b'spam'")
B = b'spam'

print()
print('type(S) =', type(S))
print('type(B) =', type(B))

print()
print('S[0] =', S[0])
print('B[0] =', B[0])

print()
print('S[1:] =', S[1:])
print('B[1:] =', B[1:])

print()
print('list(S) =', list(S))
print('list(B) =', list(B))

print()
print('S.encode() =', S.encode())
print("bytes(S, encoding = 'ascii') =", bytes(S, encoding = 'ascii'))

print()
print('B.decode() =', B.decode())
print("str(B, encoding = 'ascii') =", str(B, encoding = 'ascii'))

'''
error!!!
TypeError: 'str' object does not support item assignment
S[0] = 1

TypeError: 'bytes' object does not support item assignment
B[0] = 1
'''
