class First_class:
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)

class Second_class(First_class):
    def display(self):
        print('Second_class, self.data =', self.data)

class Third_class(Second_class):
    def __init__(self, value):
        self.data = value
    def __add__(self, other):
        return Third_class(self.data + other)
    def __str__(self):
        return '[Third_class: %s]' % self.data
    def mul(self, other):
        self.data *= other

print("a = Third_class('abc')")
a = Third_class('abc')
print('a =', a)

print('a.display()')
a.display()

print('')
print('a.mul(3)')
a.mul(3)
print('a.display()')
a.display()

print('')
print("b = a + '123'")
b = a + '123'
print('b =', b)

print('b.display()')
b.display()

print('')
print("c = Third_class(11)")
c = Third_class(11)
print('c =', c)

print('c.display()')
c.display()

print('')
print('c.mul(3)')
c.mul(3)
print('c.display()')
c.display()

print('')
print("d = c + 100")
d = c + 100
print('d =', d)

print('d.display()')
d.display()

print('')
print('每个实例都可以通过__class__属性查看创建自己的类')
print('d.__class__ =', d.__class__)

print('')
print('每个类都可以通过__bases__属性查看自己的超类')
print('Third_class.__bases__ =', Third_class.__bases__)
