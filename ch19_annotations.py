print('def func0(a, b, c)')
def func0(a, b, c):
    return a + b + c
#print('dir(func0) =', dir(func0))
print('func0.__annotations__ =', func0.__annotations__)
print('func0(1, 2, 3) =', func0(1, 2, 3))

print('*' * 30)
print("def func1(a: 'spam', b: (1, 10), c: float) -> int")
def func1(a: 'spam', b: (1, 10), c: float) -> int:
    return a + b + c
#print('dir(func1) =', dir(func1))
print('func1.__annotations__ =', func1.__annotations__)
print('func1(1, 2, 3) =', func1(1, 2, 3))

print('*' * 30)
print("def func2(a: 'spam' = 4, b: (1, 10) = 5, c: float = 6) -> int")
def func2(a: 'spam' = 4, b: (1, 10) = 5, c: float = 6) -> int:
    return a + b + c
print('func2.__annotations__ =', func2.__annotations__)
print('func2() =', func2())
