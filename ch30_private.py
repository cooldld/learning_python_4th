print('没有伪私有属性的例子')

print()
print('class c_c1')
class c_c1:
    def meth1(self):
        self.x = 88
        print('c_c1.meth1(), self.x =', self.x)
    def meth2(self):
        print('c_c1.meth2(), x =', self.x)

print()
print('class c_c2')
class c_c2:
    def metha(self):
        self.x = 99
        print('c_c2.metha(), self.x =', self.x)
    def methb(self):
        print('c_c2.methb(), x =', self.x)

print()
print('class c_c3(c_c1, c_c2): pass')
class c_c3(c_c1, c_c2): pass

print()
print('data = c_c3()')
data = c_c3()

print()
print('data.meth1()')
data.meth1()
print('data.metha()')
data.metha()
print('data.meth2()')
data.meth2()
print('data.__dict__ =', data.__dict__)

print()
print('data.metha()')
data.metha()
print('data.meth1()')
data.meth1()
print('data.methb()')
data.methb()
print('data.__dict__ =', data.__dict__)

print()
print('使用伪私有属性的例子')

print()
print('class c_c1')
class c_c1:
    def meth1(self):
        self.__x = 88
        print('c_c1.meth1(), self.__x =', self.__x)
    def meth2(self):
        print('c_c1.meth2(), x =', self.__x)

print()
print('class c_c2')
class c_c2:
    def metha(self):
        self.__x = 99
        print('c_c2.metha(), self.__x =', self.__x)
    def methb(self):
        print('c_c2.methb(), x =', self.__x)

print()
print('class c_c3(c_c1, c_c2): pass')
class c_c3(c_c1, c_c2): pass

print()
print('data = c_c3()')
data = c_c3()

print()
print('data.meth1()')
data.meth1()
print('data.metha()')
data.metha()
print('data.meth2()')
data.meth2()
print('data.__dict__ =', data.__dict__)

print()
print('data.metha()')
data.metha()
print('data.meth1()')
data.meth1()
print('data.methb()')
data.methb()
print('data.__dict__ =', data.__dict__)
