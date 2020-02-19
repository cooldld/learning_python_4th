print('def func(x, y, z)')
def func(x, y, z): return x + y + z

print('func(2, 3, 4) =', func(2, 3, 4))

print('\nf = lambda x, y, z: x + y + z')
f = lambda x, y, z: x + y + z
print('f(2, 3, 4) =', f(2, 3, 4))

print("\nf = lambda x = 'fee', y = 'fie', z = 'foe': x + y + z")
f = lambda x = 'fee', y = 'fie', z = 'foe': x + y + z
print("f('hello') =", f('hello'))

L = [lambda x: x ** 2,
    lambda x: x ** 3,
    lambda x: x ** 4]

print('\nL =', L)
for f in L:
    print('f(2) =', f(2))

print('\nlower = lambda x, y: x if x < y else y')
lower = lambda x, y: x if x < y else y
print("lower(17, 3) =", lower(17, 3))
print("lower('aa', 'bb') =", lower('aa', 'bb'))

#在lambda中执行循环
import sys

print('\nshowall = lambda x: list(map(sys.stdout.write, x))')
showall = lambda x: list(map(sys.stdout.write, x))
print(r"showall(['aa\n', 'bb\n', 'cc\n'])")
showall(['aa\n', 'bb\n', 'cc\n'])

print('\nshowall = lambda x: [sys.stdout.write(line) for line in x]')
showall = lambda x: [sys.stdout.write(line) for line in x]
print(r"showall(['aa\n', 'bb\n', 'cc\n'])")
showall(['aa\n', 'bb\n', 'cc\n'])

#嵌套lambda和作用域
print('\ndef action(x)')
def action(x):
    return (lambda y: x + y)
act = action(99)
print('act = action(99), act =', act)
print('act(2) =', act(2))

print('\naction = (lambda x: (lambda y: x + y))')
action = (lambda x: (lambda y: x + y))
act = action(99)
print('act = action(99), act =', act)
print('act(2) =', act(2))
