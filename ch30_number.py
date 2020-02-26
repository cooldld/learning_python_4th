print('class c_number, def double/triple')
class c_number:
    def __init__(self, base):
        self.base = base
    def double(self):
        print('c_number.double(), base =', self.base)
        return self.base * 2
    def triple(self):
        print('c_number.triple(), base =', self.base)
        return self.base * 3
    def unbound_xxx():
        pass

print()
print('x = c_number(2)')
x = c_number(2)
print('y = c_number(3)')
y = c_number(3)
print('z = c_number(4)')
z = c_number(4)

print()
print('acts = [x.double, y.double, y.triple, z.double]')
acts = [x.double, y.double, y.triple, z.double]
for x in acts:
    print('x() = %s, x = %s' % (x(), x))
