class first_class:
    def setdata(self, value):
        self.data = value
    def display(self):
        print('first_class, self.data =', self.data)

class second_class(first_class):
    def display(self):
        print('second_class, self.data =', self.data)

class third_class(first_class): pass

s = second_class()
t = third_class()

s.setdata(42)
t.setdata(42)

print('s.display()')
s.display()

print()
print('t.display()')
t.display()
