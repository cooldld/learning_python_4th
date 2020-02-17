def func(n):
    action = (lambda x: x ** n)
    return action

f = func(2)
print('f = func(2), f =', f)
print('f(2) =', f(2))
print('f(3) =', f(3))
g = func(3)
print('g = func(3), g =', g)
print('g(2) =', g(2))
print('g(3) =', g(3))

def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x: i ** x)
    return acts

acts = makeActions()
print('makeActions(), acts =', acts)
print('acts[0](2) =', acts[0](2))
print('acts[1](2) =', acts[1](2))
print('acts[2](2) =', acts[2](2))
print('acts[3](2) =', acts[3](2))
print('acts[4](2) =', acts[4](2))


def makeActions2():
    acts = []
    for i in range(5):
        acts.append(lambda x, i = i: i ** x) #diff from makeActions
    return acts

acts = makeActions2()
print('makeActions2(), acts =', acts)
print('acts[0](2) =', acts[0](2))
print('acts[1](2) =', acts[1](2))
print('acts[2](2) =', acts[2](2))
print('acts[3](2) =', acts[3](2))
print('acts[4](2) =', acts[4](2))

def f1():
    x = 99
    def f2():
        def f3():
            print('f3(), x =', x)
        print('call f3()')
        f3()
    print('call f2()')
    f2()

print('call f1()')
f1()
