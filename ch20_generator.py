print('def gensquares(N)')
def gensquares(N):
    for i in range(N):
        yield i ** 2

print()
print('for i in gensquares(5)')
for i in gensquares(5):
    print(i)

print()
#gensquares返回一个生成器对象generator object
x = gensquares(5)
print('x = gensquares(5), x =', x)
print('dir(x) =', dir(x))
print('next(x) =', next(x))
print('x.__next__() =', x.__next__())
print('next(x) =', next(x))
print('x.__next__() =', x.__next__())
print('next(x) =', next(x))
print('''
error!!!
StopIteration
print('next(x) =', next(x))
or
print('x.__next__() =', x.__next__())
''')

print('*' * 30)
print('how to use send with yield')
print('def gen()')
def gen():
    for i in range(10):
        print('gen, before yield, i =', i)
        x = yield i
        print('gen, after yield, x =', x)

g = gen()
print('g = gen(), g =', g)

print('\ncall next(g)')
ret = next(g)
print('next(g) =', ret)

print('\ncall next(g)')
next(g)
print('next(g) =', ret)

print('\ncall next(g)')
next(g)
print('next(g) =', ret)

print('\ncall g.send(21)')
ret = g.send(21)
print('g.send(21) =', ret)

print('\ncall g.send(41)')
g.send(41)
print('g.send(41) =', ret)

print('\ncall next(g)')
next(g)
print('next(g) =', ret)

print('\ncall next(g)')
next(g)
print('next(g) =', ret)

print("\ncall g.send('hello')")
g.send('hello')
print("g.send('hello') =", ret)

print('\ncall next(g)')
next(g)
print('next(g) =', ret)

print('')

#生成器表达式
L = [x ** 2 for x in range(4)]
print('[x ** 2 for x in range(4)] =', L)

G = (x ** 2 for x in range(4))
print('(x ** 2 for x in range(4)) =', G)
print('next(G) =', next(G))
print('next(G) =', next(G))
print('list(G) =', list(G))

print('')
print('for num in (x ** 2 for x in range(4))')
for num in (x ** 2 for x in range(4)):
    print('num =', num)

print('')
G = (c * 4 for c in 'SPAM')
print("G = (c * 4 for c in 'SPAM'), G =", G)
print('list(G) =', list(G))

print('')
print('def timesfour(s)')
def timesfour(s):
    for c in s:
        yield c * 4

G = timesfour('SPAM')
print("G = timesfour('SPAM'), G =", G)
print('list(G) =', list(G))

#只支持一个迭代器
print('')
G = (c * 4 for c in 'SPAM')
print("G = (c * 4 for c in 'SPAM'), G =", G)
I1 = iter(G)
print('I1 = iter(G), I1 =', I1)
print('next(I1) =', next(I1))
print('next(I1) =', next(I1))
I2 = iter(G)
print('I2 = iter(G), I2 =', I2)
print('next(I2) =', next(I2))

L = [1, 2, 3, 4]
print('L =', L)
I1 = iter(L)
print('I1 = iter(L), I1 =', I1)
print('next(I1) =', next(I1))
print('next(I1) =', next(I1))
I2 = iter(L)
print('I2 = iter(L), I2 =', I2)
print('next(I2) =', next(I2))
print('next(I2) =', next(I2))
