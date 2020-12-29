print('def fetcher(obj, index)')
def fetcher(obj, index):
    return obj[index]

print()
x = 'spam'
print('x =', x)

print('fetcher(x, 3) =', fetcher(x, 3))

'''
error!!!
IndexError: string index out of range
fetcher(x, 4)
'''

print()
print('try/except 捕获异常')
print('try fetcher(x, 4)')
try:
    fetcher(x, 4)
except IndexError:
    print('exception: IndexError')

print()
print('异常处理完，后面的代码继续执行')
print('hello')

print()
print('try/finally 终止行为')
print('try fetcher(x, 3)')
try:
    fetcher(x, 3)
finally:
    print('exception: finally')
print('try fetcher(x, 3) finish')

print()
print('try/finally 终止行为')
print('try fetcher(x, 4)')
try:
    fetcher(x, 4)
finally:
    print('exception: finally')
print('try fetcher(x, 4) finish')
