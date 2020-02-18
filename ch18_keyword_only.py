print('def kwonly(a, *b, c)')
def kwonly(a, *b, c):
    print('a = %s, b = %s, c = %s' % (a, b, c))

print('call kwonly(1, 2, c = 3)')
kwonly(1, 2, c = 3)

print('call kwonly(a = 1, c = 3)')
kwonly(a = 1, c = 3)

print('''
error!!!
kwonly(1, 2, 3)
''')

#函数不会接受一个变量长度的参数列表
print('\ndef kwonly(a, *, b, c)')
def kwonly(a, *, b, c):
    print('a = %s, b = %s, c = %s' % (a, b, c))

print('call kwonly(1, c = 3, b = 2)')
kwonly(1, c = 3, b = 2)
print('call kwonly(c = 3, b = 2, a = 1)')
kwonly(c = 3, b = 2, a = 1)

print('''
error!!!
kwonly(1, 2, c = 3)
''')

print("\ndef kwonly(a, *, b = 'spam', c = 'ham')")
def kwonly(a, *, b = 'spam', c = 'ham'):
    print('a = %s, b = %s, c = %s' % (a, b, c))

print('call kwonly(1)')
kwonly(1)
print('call kwonly(1, c = 3)')
kwonly(1, c = 3)
print('call kwonly(a = 1)')
kwonly(a = 1)
print('call kwonly(c = 3, b = 2, a = 1)')
kwonly(c = 3, b = 2, a = 1)

print("\ndef kwonly(a, *, b, c = 'ham')")
def kwonly(a, *, b, c = 'ham'):
    print('a = %s, b = %s, c = %s' % (a, b, c))

print('''
error!!!
kwonly(1)
kwonly(1, c = 3)
''')

print('call kwonly(c = 3, b = 2, a = 1)')
kwonly(c = 3, b = 2, a = 1)

print('\ndef f(a, *b, c = 6, **d)')
def f(a, *b, c = 6, **d):
    print('a = %s, b = %s, c = %s, d = %s' % (a, b, c, d))

print('call f(1, *(2, 3), **dict(x = 4, y = 5))')
f(1, *(2, 3), **dict(x = 4, y = 5))

print('''
error!!!
f(1, *(2, 3), **dict(x = 4, y = 5), c = 7)
''')

print('call f(1, *(2, 3), c = 7, **dict(x = 4, y = 5))')
f(1, *(2, 3), c = 7, **dict(x = 4, y = 5))

print('call f(1, c = 7, *(2, 3), **dict(x = 4, y = 5))')
f(1, c = 7, *(2, 3), **dict(x = 4, y = 5))

print('call f(1, *(2, 3), **dict(x = 4, y = 5, c = 7))')
f(1, *(2, 3), **dict(x = 4, y = 5, c = 7))
