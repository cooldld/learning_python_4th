print('demo1:')
print("for line in open('ch07_echo.py')")
for line in open('ch07_echo.py'):
    print(line.upper(), end='')

print('\ndemo2:')
print("for line in open('ch07_echo.py').readlines()")
for line in open('ch07_echo.py').readlines():
    print(line.upper(), end='')

print('\ndemo3:')
print("while and line = f.readline()")
f = open('ch07_echo.py')
while True:
    line = f.readline()
    if not line: break
    print(line.upper(), end='')
f.close()

print('\ndemo4:')
print("call f.__next__()")
f = open('ch07_echo.py')
print('f.__next__() =', f.__next__(), end='')
print('f.__next__() =', f.__next__(), end='')
print('f.__next__() =', f.__next__(), end='')
print('f.__next__() =', f.__next__(), end='')
f.close()

print('\ndemo5:')
print("call next(f)")
f = open('ch07_echo.py')
print('next(f) =', next(f), end='')
print('next(f) =', next(f), end='')
print('next(f) =', next(f), end='')
print('next(f) =', next(f), end='')
f.close()

print('\ndemo6:')
print("call iter(f) and next(i)")
f = open('ch07_echo.py')
i = iter(f)
print('next(i) =', next(i), end='')
print('next(i) =', next(i), end='')
print('next(i) =', next(i), end='')
print('next(i) =', next(i), end='')
f.close()

print('\ndemo7:')
print("call iter(f) and i.__next__()")
f = open('ch07_echo.py')
i = iter(f)
print('i.__next__() =', i.__next__(), end='')
print('i.__next__() =', i.__next__(), end='')
print('i.__next__() =', i.__next__(), end='')
print('i.__next__() =', i.__next__(), end='')
f.close()

print('\ndemo8:')
print("try and except StopIteration")
f = open('ch07_echo.py')
i = iter(f)
while True:
    try:
        line = next(i)
    except StopIteration:
        print('catch StopIteration')
        break
    print('line =', line, end='')
f.close()
