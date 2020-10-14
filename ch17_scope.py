L = [1, 2, 3]

def def_scope1():
    L = [4, 5, 6]
    print('def_scope1, L =', L)

def def_scope2():
    global L
    print('global L =', L)
    L = [4, 5, 6]
    print('def_scope2, L =', L)

print('module, L =', L)
print('call def_scope1')
def_scope1()
print('module, L =', L)
print('call def_scope2')
def_scope2()
print('module, L =', L)

def func():
    #L = L + [4, 5]  #can not = operate
    print('L =', L)  #can use
    #x = 1
print('call func')
func()

x, y, z = 0, 1, 1
def all_global():
    global x
    x = y + z
print('x = %s, y = %s, z = %s' % (x, y, z))
print('call all_global')
all_global()
print('x = %s, y = %s, z = %s' % (x, y, z))
