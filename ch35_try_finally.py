print('def func1()')
def func1():
    try:
        print('func1, raise IndexError')
        raise IndexError
    except IndexError:
        print('func1, except IndexError')
    finally:
        print('func1, finally')

print()
print('def func2()')
def func2():
    try:
        print('func2, call func1()')
        func1()
    except IndexError:
        print('func2, except IndexError')
    finally:
        print('func2, finally')

print()
print('try and func2()')
try:
    func2()
except IndexError:
    print('main, except IndexError')
finally:
    print('main, finally')
