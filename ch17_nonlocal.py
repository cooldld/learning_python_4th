def f1():
    x = 88
    print('f1(), x =', x)
    def f2():
        x = 99
        print('f2(), x =', x)
    print('call f2()')
    f2()
    print('after f2(), x =', x)

print('call f1()')
f1()

print('-' * 3, 'use nonlocal', '-' * 3, sep='')
def f1():
    x = 88
    print('f1(), x =', x)
    def f2():
        print('nonlocal x')
        nonlocal x
        x = 99
        print('f2(), x =', x)
    print('call f2()')
    f2()
    print('after f2(), x =', x)

print('call f1()')
f1()

def tester(start):
    state = start
    def nested(label):
        print('label = %s, state = %s' % (label, state))
    return nested

print('F = tester(0)')
F = tester(0)
print("call F('spam')")
F('spam')

'''
def tester(start):
    state = start
    def nested(label):
        print('label = %s, state = %s' % (label, state))
        state += 1  #error!!!
    return nested
'''

def tester1(start):
    state = start
    def nested(label):
        nonlocal state
        print('label = %s, state = %s' % (label, state))
        state += 1
    return nested

print('F = tester1(0)')
F = tester1(0)
print("call F('spam')")
F('spam')
print("call F('ham')")
F('ham')
print("call F('eggs')")
F('eggs')

print('G = tester1(0)')
G = tester1(0)
print("call G('spam')")
G('spam')
print("call G('ham')")
G('ham')
print("call G('eggs')")
G('eggs')

print("call F('eggs')")
F('eggs')

'''
def tester1(start):
    def nested(label):
        nonlocal state
        state = 0  #error!!!
        print('label = %s, state = %s' % (label, state))
    return nested

spam = 99
def tester1(start):
    def nested(label):
        nonlocal spam  #error!!!
    return nested
'''

def tester2(start):
    def nested(label):
        global state
        state = 0
        print('label = %s, state = %s' % (label, state))
    return nested

print('F = tester2(0)')
F = tester2(0)
print("call F('spam')")
F('spam')
print("call F('ham')")
F('ham')
print("call F('eggs')")
F('eggs')
print('global state =', state)

def tester3(start):
    global state
    state = start
    def nested(label):
        global state
        print('label = %s, state = %s' % (label, state))
        state += 1
    return nested

print('F = tester3(0)')
F = tester3(0)
print('G = tester3(10)')
G = tester3(10)
print("call F('spam')")
F('spam')
print("call G('spam')")
G('spam')
print("call F('ham')")
F('ham')
print("call G('ham')")
G('ham')
print("call F('eggs')")
F('eggs')
print("call G('eggs')")
G('eggs')

class tester4:
    def __init__(self, start):
        self.state = start
    def __call__(self, label):
        print('label = %s, state = %s' % (label, self.state))
        self.state += 1

print('F = tester4(0)')
F = tester4(0)
print('G = tester4(10)')
G = tester4(10)
print("call F('spam')")
F('spam')
print("call G('spam')")
G('spam')
print("call F('ham')")
F('ham')
print("call G('ham')")
G('ham')
print("call F('eggs')")
F('eggs')
print("call G('eggs')")
G('eggs')

def tester5(start):
    def nested(label):
        print('label = %s, state = %s' % (label, nested.state))
        nested.state += 1
    nested.state = start
    return nested

print('F = tester5(0)')
F = tester4(0)
print('G = tester5(10)')
G = tester4(10)
print("call F('spam')")
F('spam')
print("call G('spam')")
G('spam')
print("call F('ham')")
F('ham')
print("call G('ham')")
G('ham')
print("call F('eggs')")
F('eggs')
print("call G('eggs')")
G('eggs')
