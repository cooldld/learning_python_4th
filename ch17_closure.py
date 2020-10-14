x = 99

def f1():
    #print(x)
    x = 88
    print('f1, x=', x)
    def f2():
        print('f2, x=', x)
    f2()

def f3():
    x = 88
    print('f3, x=', x)
    def f4():
        print('f4, x=', x)
    return f4

print('module, x=', x)
print('call f1()')
f1()
print('call f3()')
action = f3()
print('call f4()')
action()

def f5():
    L = [1, 2, 3, 4]
    print('f5(), L=', L)
    def f5_1():
        return L
    return f5_1

print('call f5()')
f5_ret = f5()
print('f5_1 =', f5_ret)
print('call f5_1()')
L1 = f5_ret()
print('f5_1(), L1=', L1)
L2 = f5_ret()
print('f5_1(), L2=', L2)
L1[0] = 10
print('L1[0] = 10, L1 =', L1, ', L2 =', L2)
L3 = f5_ret()
print('f5_1(), L3=', L3)

print()
print('maker是工厂函数, 也叫闭合closure函数')
def maker(n):
    def action(x):
        print('{0} ** {1}'.format(x, n))
        return x ** n
    return action

f = maker(2)
print('f = maker(2), f =', f)
g = maker(3)
print('g = maker(3), g =', g)

print('f(2) =', f(2))
print('g(2) =', g(2))
print('f(3) =', f(3))
print('g(3) =', g(3))
