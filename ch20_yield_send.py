'''
理解Python的yield与send()语句
https://blog.csdn.net/levon2018/article/details/82492240

next()跟send()不同的地方是，next()只能以None作为参数传递，而send()可以传递yield的值
n = yield r可以理解为yield在发送n的同时也在接收r值
通过produce(c)调用后，一旦有n值，则切换到 consumer去执行。执行完了后生成器关闭
'''

def cf(x):
    for i in range(x):
        print('before yield, x={0}, i={1}'.format(x, i))
        n = yield i
        print('after yield, x={0}, i={1}, n={2}'.format(x, i, n))

g = cf(5)
print('g = cf(5), g =', g)

print()
print('必须通过send(None)来启动生成器')
print('call g.send(None)')
ret = g.send(None)
print('ret =', ret)

print()
print("call g.send('a')")
ret = g.send('a')
print('ret =', ret)

print()
print("call g.send('b')")
ret = g.send('b')
print('ret =', ret)

print()
print("call g.send('c')")
ret = g.send('c')
print('ret =', ret)

print()
print("call g.send('d')")
ret = g.send('d')
print('ret =', ret)

'''
StopIteration
print("call g.send('e')")
ret = g.send('e')
print('ret =', ret)
'''
