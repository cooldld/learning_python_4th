print('class C2')
class C2: pass

print('class C3')
class C3: pass

print('class C1(C2, C3)')
class C1(C2, C3):
    def setname(self, who):
        self.name = who #对特殊参数self做赋值操作，可以把属性添加到实例中

print('')
print('I1 = C1()')
I1 = C1()
print('''
error!!!
AttributeError: 'C1' object has no attribute 'name'
print('I1.name =', I1.name)
''')
print("I1.setname('bob')")
I1.setname('bob')
print('I1.name =', I1.name)

print('')
print('I2 = C1()')
I2 = C1()
print('''
error!!!
AttributeError: 'C1' object has no attribute 'name'
print('I2.name =', I2.name)
''')

print("I2.setname('tom')")
I2.setname('tom')
print('I2.name =', I2.name)
print('I1.name =', I1.name)
