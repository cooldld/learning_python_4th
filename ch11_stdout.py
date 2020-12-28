print('use sys.stdout.write')

import sys
sys.stdout.write('hello world\n')

stdout_default = sys.stdout

file_name = 'ch11_stdout.data'

print('sys.stdout = open', file_name)
sys.stdout = open(file_name, 'a')
print('hello world')
print(1, 2, 3)
print('sys.stdout.close')
sys.stdout.close()

#a error happen
#print(1, 2, 3)

sys.stdout = stdout_default
print('sys.stdout is default')
print(1, 2, 3)

print('print(file=log)')
log = open(file_name, 'a')
print('sys.stdout is default', file=log)
print(1, 2, 3, file=log)
