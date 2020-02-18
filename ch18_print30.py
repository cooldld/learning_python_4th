import sys

print('def print30(*args, **kargs)')
def print30(*args, **kargs):
    sep = kargs.get('sep', ' ')
    end = kargs.get('end', '\n')
    file = kargs.get('file', sys.stdout)
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)

print("call print30(1, 2, 3)")
print30(1, 2, 3)
print("call print30(1, 2, 3, sep='')")
print30(1, 2, 3, sep='')
print("call print30(1, 2, 3, sep='...')")
print30(1, 2, 3, sep='...')
print("call print30(1, [2], (3,), sep='...')")
print30(1, [2], (3,), sep='...')
print("call print30(4, 5, 6, sep='', end='')")
print30(4, 5, 6, sep='', end='')
print("call print30(7, 8, 9)")
print30(7, 8, 9)
print("call print30()")
print30()
print(r"call print30(1, 2, 3, sep='??', end='.\n', file=sys.stderr)")
print30(1, 2, 3, sep='??', end='.\n', file=sys.stderr)

#use keyword-only args
print()
print(r"def print30(*args, sep = ' ', end = '\n', file = sys.stdout)")
def print30(*args, sep = ' ', end = '\n', file = sys.stdout):
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)

print('''
error!!!
print30(99, name='bob')
''')

print('\ndef print30(*args, **kargs)')
def print30(*args, **kargs):
    sep = kargs.pop('sep', ' ')
    end = kargs.pop('end', '\n')
    file = kargs.pop('file', sys.stdout)
    if kargs: raise TypeError('extra keywords: %s' % kargs)
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)

print("call print30(99, name='bob')")
print30(99, name='bob')
