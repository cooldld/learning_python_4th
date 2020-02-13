print('list(range(5)) =', list(range(5)))
print('list(range(2, 5)) =', list(range(2, 5)))
print('list(range(0, 10, 2)) =', list(range(0, 10, 2)))
print('list(range(-5, 5)) =', list(range(-5, 5)))
print('list(range(5, -5, -1)) =', list(range(5, -5, -1)))

print('for i in range(3)')
for i in range(3):
    print('i =', i)

print("for i in 'spam'")
for i in 'spam':
    print('i =', i)

s = 'abcdefghijk'
print('s =', s)
print("for i in s[::2]: print('i =', i)")
for i in s[::2]: print('i =', i)
