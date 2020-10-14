'''
在python中实现c语言的__FILE__, __LINE__, __FUNC__
https://blog.csdn.net/u012939880/article/details/103288568
'''

import inspect

def __LINE__():
    stack = inspect.stack()
    info = inspect.getframeinfo(stack[1][0])
    return info.lineno

def __FUNC__():
    stack = inspect.stack()
    info = inspect.getframeinfo(stack[1][0])
    return info.function

def __FILE__():
    stack = inspect.stack()
    info = inspect.getframeinfo(stack[1][0])
    return info.filename
