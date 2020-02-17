print('def f(a, b, c)')
def f(a, b, c): print('a = %s, b = %s, c = %s' % (a, b, c))

print('call f(1, 2, 3)')
f(1, 2, 3)

print('call f(c = 3, b = 2, a = 1)')
f(c = 3, b = 2, a = 1)

'''
f(c = 3, 1, b = 2)  #error!!!
f(c = 3, b = 2, 1)  #error!!!
'''

print('call f(1, c = 3, b = 2)')
f(1, c = 3, b = 2)

print('def f(a, b = 2, c = 3)')
def f(a, b = 2, c = 3): print('a = %s, b = %s, c = %s' % (a, b, c))

print('call f(1)')
f(1)
print('call f(1, 20)')
f(1, 20)
print('call f(1, 20, 30)')
f(1, 20, 30)
print('call f(1, c=33)')
f(1, c=33)

print('def f(a, b, c = 0, d = 0)')
def f(a, b, c = 0, d = 0): print('a = %s, b = %s, c = %s, d = %s' % (a, b, c, d))

print('call f(1, 2)')
f(1, 2)
print('call f(1, d = 1, b = 0)')
f(1, d = 1, b = 0)
print('call f(a = 1, b = 0)')
f(a = 1, b = 0)
print('call f(c = 1, b = 2, a = 3)')
f(c = 1, b = 2, a = 3)
print('call f(1, 2, 3, 4)')
f(1, 2, 3, 4)
#print('call f')
