print()

x = 'spam'
y = 99
z = ['eggs']

print(x, y, z)

print(x, y, z, sep='')

print(x, y, z, sep=', ')

print(x, y, z, end='')

print(x, y, z, end=''); print(x, y, z)

print(x, y, z, end='...\n')

print(x, y, z, sep='...', end='!\n')

print(x, y, z, end='!\n', sep='...')

file_name = 'ch11_print.data'
print('file_name =', file_name)
print(x, y, z, sep='...', file=open(file_name, 'w'))

print(x, y, z)

print(open(file_name, 'r').read())

text = '%s: %-.4f, %05d' % ('Result', 3.14159, 42)
print(text)

print('%s: %-.4f, %05d' % ('Result', 3.14159, 42))
