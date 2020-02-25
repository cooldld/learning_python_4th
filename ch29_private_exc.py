class PrivateExc(Exception): pass

print('class Privacy, def __setattr__')
class Privacy:
    def __setattr__(self,attrname, value):
        if attrname in self.privates:
            raise PrivateExc(attrname, self)
        else:
            self.__dict__[attrname] = value

print()
print('class Test1(Privacy)')
class Test1(Privacy):
    privates = ['age']

print()
print('class Test2(Privacy)')
class Test2(Privacy):
    privates = ['name', 'pay']
    def __init__(self):
        self.__dict__['name'] = 'Tom'

print()
print('x = Test1()')
x = Test1()
print('y = Test2()')
y = Test2()

print()
print("x.name = 'Bob'")
x.name = 'Bob'

print('''
error!!!
__main__.PrivateExc: ('name', <__main__.Test2 object at 0xb703bb6c>)
y.name = 'Sue'

__main__.PrivateExc: ('age', <__main__.Test1 object at 0xb707fb2c>)
x.age = 30
''')

print('y.age = 40')
y.age = 40
