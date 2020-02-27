print('class c_x, attr a = 1')
class c_x:
    a = 1

print()
print('x = c_x()')
x = c_x()
print('c_x.a =', c_x.a)
print('x.a =', x.a)

print()
print('修改了c_x类的属性a')
print('set c_x.a = 3')
c_x.a = 3

print()
print('c_x.a =', c_x.a)
print('x.a =', x.a)

print()
print('修改了c_x类实例x的属性a')
print('set x.a = 5')
x.a = 5

print()
print('c_x.a =', c_x.a)
print('x.a =', x.a)

print()
print('class c_x: pass')
class c_x: pass

print()
print('x = c_x()')
x = c_x()
print('c_x类实例x添加了属性a')
print('set x.a = 1')
x.a = 1
print('x.a =', x.a)

print()
print('c_x类添加了属性a')
print('set c_x.a = 3')
c_x.a = 3
print('c_x.a =', c_x.a)
print('x.a =', x.a)
