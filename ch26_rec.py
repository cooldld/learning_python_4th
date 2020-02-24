print('class rec: pass')
class rec: pass
print('dir(rec) =', dir(rec))

print("rec.name = 'bob'")
rec.name = 'bob'
print('rec.age = 40')
rec.age = 40
print('dir(rec) =', dir(rec))

print('x = rec()')
x = rec()
print('x.name =', x.name)
print("x.name = 'hello'")
x.name = 'hello'
print('x.name =', x.name)

print('y = rec()')
y = rec()

print('')
print('rec.name = %s, x.name = %s, y.name = %s' % (rec.name, x.name, y.name))

print('')
print('类的字典信息中只会显示已经赋值了的属性')
print('rec.__dict__.keys =', list(rec.__dict__.keys()))
print('x.__dict__.keys =', list(x.__dict__.keys()))
print('y.__dict__.keys =', list(y.__dict__.keys()))

print('')
print('def upper_name(self)')
def upper_name(self):
    return self.name.upper();

print('uppter_name(x) =', upper_name(x))

print('')
print('通过手工赋值，给rec类添加了属性upper_name方法')
print('rec.upper_name = uppper_name')
rec.upper_name = upper_name

print('x.upper_name() =', x.upper_name())
print('y.upper_name() =', y.upper_name())
print('rec.upper_name(x) =', rec.upper_name(x))
