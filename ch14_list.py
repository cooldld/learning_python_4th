L = [1, 2, 3, 4, 5]

print('L =', L)

L = [x + 10 for x in L]
print('[x + 10 for x in L] =', L)

L = [1, 2, 3, 4, 5]
L = [x + 10 for x in L if x > 2]
print('[x + 10 for x in L if x > 2] =', L)

L = [x + y for x in 'abc' for y in '123']
print("[x + y for x in 'abc' for y in '123'] =", L)

L = [line.rstrip() for line in  open('ch07_echo.py')]
print("[line.rstrip() for line in  open('ch07_echo.py')] =", L)

L = [line.upper() for line in  open('ch07_echo.py')]
print("[line.upper() for line in  open('ch07_echo.py')] =", L)

L = [line.rstrip().upper() for line in  open('ch07_echo.py')]
print("[line.rstrip().upper() for line in  open('ch07_echo.py')] =", L)

L = [('sys' in line, line[0]) for line in  open('ch07_echo.py')]
print("[('sys' in line, line[0]) for line in  open('ch07_echo.py')] =", L)

L = [line.rstrip() for line in  open('ch07_echo.py') if line[0] == 'p']
print("[line.rstrip() for line in  open('ch07_echo.py') if line[0] == 'p'] =", L)
