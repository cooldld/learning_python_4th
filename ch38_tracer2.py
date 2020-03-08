calls = 0

print('def tracer(func, *args)')
def tracer(func, *args):
    global calls
    calls += 1
    print('tracer, calls =', calls)
    func(*args)

print()
print('def spam(a, b, c)')
def spam(a, b, c):
    print('spam, a + b + c =', a + b + c)

print()
print('spam =', spam)

print()
print('tracer(spam, 1, 2, 3)')
tracer(spam, 1, 2, 3)

print()
print("tracer(spam, 'a', 'b', 'c')")
tracer(spam, 'a', 'b', 'c')
