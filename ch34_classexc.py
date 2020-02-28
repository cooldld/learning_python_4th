print('class c_general(Exception): pass')
class c_general(Exception): pass

print('class c_specific1(c_general): pass')
class c_specific1(c_general): pass

print('class c_specific2(c_general): pass')
class c_specific2(c_general): pass

print()
print('def raise_general')
def raise_general():
    x = c_general()
    raise x

print()
print('def raise_specific1')
def raise_specific1():
    x = c_specific1()
    raise x

print()
print('def raise_specific2')
def raise_specific2():
    x = c_specific2()
    raise x

print()
print('for func in (raise_general, raise_specific1, raise_specific2)')
print('except c_general')
for func in (raise_general, raise_specific1, raise_specific2):
    try:
        func()
    except c_general:
        import sys
        print('exception', sys.exc_info()[0])
