from ch00_file_line_func import __FUNC__,__FILE__,__LINE__

def funcxxx(a):
    b = 'spam'
    print(__FUNC__(),__FILE__(),__LINE__())
    return b * a

func = funcxxx
print('func(8) =', func(8))

print('func.__name__ =', func.__name__)
print('dir(func) =', dir(func))
print('func.__code__ =', func.__code__)
print('dir(func.__code__) =', dir(func.__code__))
print('func.__code__.co_varnames =', func.__code__.co_varnames)
print('func.__code__.co_argcount =', func.__code__.co_argcount)

#给函数添加属性
print('add func.count and func.handles')
func.count = 0
func.count += 1
func.handles = 'hello'
print('dir(func) =', dir(func))
