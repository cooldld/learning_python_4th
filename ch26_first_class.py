exec_str = '''
class first_class:
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)

x = first_class()
'''

print(exec_str)
exec(exec_str)

print('''
error!!!
AttributeError: 'first_class' object has no attribute 'data'
x.display()
''')

print("x.setdata('king arthur')")
x.setdata('king arthur')
print('x.display()')
x.display()

#在实例对象上添加属性
print("x.anothername = 'spam'")
x.anothername = 'spam'
print('x.anothername =', x.anothername)

print('')
print('y = first_class()')
y = first_class()
print('y.setdata(3.1415)')
y.setdata(3.1415)
print('y.display()')
y.display()
