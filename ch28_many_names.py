x = 11

def f():
    print('f(), x =', x)

def g():
    print('g(), set x to 22')
    x = 22
    print('g(), x =', x)

class C:
    #print('class C, set x to 33')
    x = 33
    def m(self):
        print('C.m(), set x to 44')
        x = 44
        print('C.m(), set self.x to 55')
        self.x = 55

if __name__ == '__main__':
    print('self test')
    print('x =', x)
    print('call f()')
    f()
    print('call g()')
    g()
    print('x =', x)
    print('obj = C()')
    obj = C()
    print('obj.x =', obj.x)
    print('call obj.m()')
    obj.m()
    print('obj.x =', obj.x)
    print('C.x =', C.x)
