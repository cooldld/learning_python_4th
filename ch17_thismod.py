#ch17_thismod.py

var = 99

def local():
    print('local, var = 0')
    var = 0

def glob1():
    print('glob1, global var += 1')
    global var
    var += 1

def glob2():
    print('glob2, import ch17_thismod, ch17_thismod.var += 1')
    var = 0
    import ch17_thismod
    ch17_thismod.var += 1

def glob3():
    print('glob2, import sys, sys.modules[ch17_thismod].var += 1')
    var = 0
    import sys
    glob = sys.modules['ch17_thismod']
    glob.var += 1

def test():
    print('init, var =', var)
    local()
    print('after local, var =', var)
    glob1()
    print('after glob1, var =', var)
    glob2()
    print('after glob2, var =', var)
    glob3()
    print('after glob3, var =', var)

'''
how to run
import ch17_thismod
ch17_thismod.test()
'''
