file_name = 'ch04_data.txt'

print('open and write file', file_name)
f = open(file_name, 'w')
print('dir(f) =', dir(f))
print('type(f) =', type(f))
f.write('Hello\n');
f.write('world\n');
f.close()

print('open and read file', file_name)
f = open(file_name, 'r')
text = f.read()
f.close()
print('text =', text )
