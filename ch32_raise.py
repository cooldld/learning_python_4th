print('用raise引发异常')
try:
    print('raise IndexError')
    raise IndexError
except IndexError:
    print('exception: IndexError')

print()
print('用assert引发异常')
try:
    print("assert False, 'a error by assert'")
    assert False, 'a error by assert'
except AssertionError:
    print('exception: AssertionError')


