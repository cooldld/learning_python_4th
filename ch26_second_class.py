print('class first_class')
class first_class:
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)

print('')
print('class second_class(first_class)')
class second_class(first_class):
    def display(self):
        print('second_class, self.data =', self.data)

z = second_class()

print('''
error!!!
AttributeError: 'second_class' object has no attribute 'data'
z.display()
''')

print('z.setdata(42)')
z.setdata(42)

print('z.display()')
z.display()
