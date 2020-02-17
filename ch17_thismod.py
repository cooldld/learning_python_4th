#ch17_thismod.py

var = 99

def local():
    #print('local(), var =', var)  #error
    var = 0

local()

def glob1():
    global var
    var += 1

def glob2():
    var = 0
    import ch17_thismod
    ch17_thismod.var += 1

def glob3():
    var = 0
    import sys
    glob = sys.modules['ch17_thismod']
    glob.var += 1

def test():
    print(var)
    local(); glob1(); glob2(); glob3()
    print(var)
