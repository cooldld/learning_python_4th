count = 0

print('def decorator(func)')
def decorator(func):
    global count
    count += 1
    print('decorator, count =', count)
    return func

print('decorator =', decorator)

print()
print('@decorator')
print('def times(x)')
@decorator
def times(x):
    print('times, x =', x)

print('times =', times)

times(1)
times(2)
times(3)
times(4)
