print('class c_general(Exception): pass')
class c_general(Exception): pass

print('class c_specific1(c_general): pass')
class c_specific1(c_general): pass

print('class c_specific2(c_general): pass')
class c_specific2(c_general): pass

print('class c_specific3(c_specific2): pass')
class c_specific3(c_specific2): pass

print()
print('def raise_general(): raise c_general()')
def raise_general(): raise c_general()

print()
print('def raise_specific1(): raise c_specific1()')
def raise_specific1(): raise c_specific1()

print()
print('def raise_specific2(): raise c_specific2()')
def raise_specific2(): raise c_specific2()

print()
print('def raise_specific3(): raise c_specific3()')
def raise_specific3(): raise c_specific3()

print()
print('for func in (raise_general, raise_specific1, raise_specific2, raise_specific3)')
print('except c_general as x')
for func in (raise_general, raise_specific1, raise_specific2, raise_specific3):
    try:
        func()
    except c_general as x:
        print('exception', x.__class__)
