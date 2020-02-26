print('class c_eggs, def m1/m2')
class c_eggs:
    def m1(self, n):
        print('c_eggs.m1(), n =', n)
    def m2(self):
        print('c_eggs.m2(), x = self.m1')
        x = self.m1
        print('c_eggs.m2(), x(42)')
        x(42)

print()
print('c_eggs().m2()')
c_eggs().m2()
