print('def f(a, b, c)')
def f(a, b, c): print('a = %s, b = %s, c = %s' % (a, b, c))

print('call f(1, 2, 3)')
f(1, 2, 3)

print('call f(c = 3, b = 2, a = 1)')
f(c = 3, b = 2, a = 1)

'''
error!!!
f(c = 3, 1, b = 2)
f(c = 3, b = 2, 1)
'''

print('call f(1, c = 3, b = 2)')
f(1, c = 3, b = 2)

print('\ndef f(a, b = 2, c = 3)')
def f(a, b = 2, c = 3): print('a = %s, b = %s, c = %s' % (a, b, c))

print('call f(1)')
f(1)
print('call f(1, 20)')
f(1, 20)
print('call f(1, 20, 30)')
f(1, 20, 30)
print('call f(1, c=33)')
f(1, c=33)

print('\ndef f(a, b, c = 0, d = 0)')
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

print('\ndef f(*args)')
def f(*args): print('*args =', args)

print('call f()')
f()
print('call f(1)')
f(1)
print('call f(1, 2, 3, 4)')
f(1, 2, 3, 4)

print('\ndef f(**args)')
def f(**args): print('**args =', args)

print('call f()')
f()
print('call f(c = 1, b = 2, a = 3)')
f(c = 1, b = 2, a = 3)

print('\ndef f(a, *pargs, **kargs)')
def f(a, *pargs, **kargs): print('a = %s, *pargs = %s, **kargs = %s' % (a, pargs, kargs))

print('call f(1, 2, 3, x=1, y=2)')
f(1, 2, 3, x=1, y=2)

print('\ndef f(a, b, c, d)')
def f(a, b, c, d): print('a = %s, b = %s, c = %s, d = %s' % (a, b, c, d))
args = (1, 2)
args += (3, 4)
print('args =', args)
print('call f(*args)')
f(*args)

args = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print('args =', args)
print('call f(**args)')
f(**args)
'''
error!!!
args = {'aa': 1, 'bb': 2, 'cc': 3, 'dd': 4}
print('args =', args)
print('call f(**args)')
f(**args)
'''
print("call f(*(1, 2), **{'d': 4, 'c': 3})")
f(*(1, 2), **{'d': 4, 'c': 3})
print("call f(1, *(2, 3), **{'d': 4})")
f(1, *(2, 3), **{'d': 4})
print("call f(1, c = 3, *(2,), **{'d': 4})")
f(1, c = 3, *(2,), **{'d': 4})
print('call f(1, *(2, 3), d = 4)')
f(1, *(2, 3), d = 4)
print("call f(1, *(2,), c = 3, **{'d': 4})")
f(1, *(2,), c = 3, **{'d': 4})

#accept arbitrary arguments
print('\ndef tracer(func, *pargs, **kargs)')
def tracer(func, *pargs, **kargs):
    print('func.__name__ =', func.__name__)
    print('call func(*pargs, **kargs)')
    func(*pargs, **kargs)
print('call tracer(f, 1, 2, c = 3, d = 4)')
tracer(f, 1, 2, c = 3, d = 4)
'''
error!!!
tracer(f, 1, 2, 5, c = 3, d = 4)
'''

#print('call f')
#print("call f")
