print('函数定义时，*args表示将参数收集到一个元组中，*args后面的参数都是keyword-only参数')
print('def kwonly(a, *b, c)')
def kwonly(a, *b, c):
    print('a = %s, b = %s, c = %s' % (a, b, c))

print('call kwonly(1, 2, c = 3)')
kwonly(1, 2, c = 3)

print('call kwonly(1, 2, 20, 22, c = 3)')
kwonly(1, 2, 20, 22, c = 3)

print('call kwonly(a = 1, c = 3)')
kwonly(a = 1, c = 3)
print('call kwonly(1, c = 3)')
kwonly(1, c = 3)
print('函数调用时，一旦出现了位置乱序的关键字参数name=value，那么后面的入参也必须是关键字参数形式')
print('call kwonly(c = 3, a = 1)')
kwonly(c = 3, a = 1)

'''
error!!!
SyntaxError: non-keyword arg after keyword arg
kwonly(c = 3, 1)
kwonly(c = 3, 1, a = 2)
kwonly(1, c = 3, 2, 20, 22)

TypeError: kwonly() missing 1 required keyword-only argument: 'c'
kwonly(1, 2, 3)
'''

print('*' * 30)
print('函数定义时，单个*的参数，表示函数不接受一个变量长度的参数列表')
print('def kwonly(a, *, b, c)')
def kwonly(a, *, b, c):
    print('a = %s, b = %s, c = %s' % (a, b, c))

print('call kwonly(1, c = 3, b = 2)')
kwonly(1, c = 3, b = 2)
print('call kwonly(c = 3, b = 2, a = 1)')
kwonly(c = 3, b = 2, a = 1)

'''
error!!!
TypeError: kwonly() takes 1 positional argument but 2 positional arguments (and 1 keyword-only argument) were given
kwonly(1, 2, c = 3)

TypeError: kwonly() got an unexpected keyword argument 'd'
kwonly(1, b = 2, c = 3, d = 10)
kwonly(1, d = 10, b = 2, c = 3)
'''

print('*' * 30)
print("def kwonly(a, *, b = 'spam', c = 'ham')")
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

print('*' * 30)
print("def kwonly(a, *, b, c = 'ham')")
def kwonly(a, *, b, c = 'ham'):
    print('a = %s, b = %s, c = %s' % (a, b, c))

'''
error!!!
TypeError: kwonly() missing 1 required keyword-only argument: 'b'
kwonly(1)
kwonly(1, c = 3)
'''

print('call kwonly(c = 3, b = 2, a = 1)')
kwonly(c = 3, b = 2, a = 1)

print('*' * 30)
print('函数定义时，keyword-only参数，必须在*args之后，在**args之前')
print('函数定义时，**args表示将关键字参数收集到一个字典中')
print('def f(a, *b, c = 6, **d)')
def f(a, *b, c = 6, **d):
    print('a = %s, b = %s, c = %s, d = %s' % (a, b, c, d))

print('call f(1, *(2, 3), **dict(x = 4, y = 5))')
f(1, *(2, 3), **dict(x = 4, y = 5))

'''
error!!!
SyntaxError: invalid syntax
f(1, *(2, 3), **dict(x = 4, y = 5), c = 7)
'''

print('call f(1, *(2, 3), c = 7, **dict(x = 4, y = 5))')
f(1, *(2, 3), c = 7, **dict(x = 4, y = 5))

print('函数调用时，keyword-only参数，可以在*args之前或之后')
print('函数调用时，keyword-only参数，一定要在**args之前或包含在**args中')
print('函数调用时，*args表示将元组入参解包后再传递给函数')
print('函数调用时，**args表示将字典入参解包后再传递给函数')
print('call f(1, c = 7, *(2, 3), **dict(x = 4, y = 5))')
f(1, c = 7, *(2, 3), **dict(x = 4, y = 5))

print('call f(1, *(2, 3), **dict(x = 4, y = 5, c = 7))')
f(1, *(2, 3), **dict(x = 4, y = 5, c = 7))
