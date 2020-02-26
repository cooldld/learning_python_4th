print('class Truth, def __bool__ with True')
class Truth:
    def __bool__(self): return True

print()
print('x = Truth()')
x = Truth()

print('bool(x) =', bool(x))

print()
print('class Truth, def __bool__ with False')
class Truth:
    def __bool__(self): return False

print()
print('x = Truth()')
x = Truth()

print('bool(x) =', bool(x))

print()
print('class Truth, def __len__ with 0')
class Truth:
    def __len__(self): return 0

print()
print('x = Truth()')
x = Truth()

print('bool(x) =', bool(x))

print()
print('class Truth, def __len__ with 1')
class Truth:
    def __len__(self): return 1

print()
print('x = Truth()')
x = Truth()

print('bool(x) =', bool(x))

print()
print('class Truth, def __bool__ with True, def __len__ with 0')
class Truth:
    def __bool__(self): return True
    def __len__(self): return 0

print()
print('x = Truth()')
x = Truth()

print('bool(x) =', bool(x))
