x, y, z = 43, 44, 45
s = 'spam'
d = {'a': 1, 'b': 2}
l = [1, 2, 3]

f = open('ch09_data.txt', 'w')
f.write(s + '\n')
f.write('%s,%s,%s\n' % (x, y, z))
f.write(str(l) +  '\n')
f.write(str(d) + '\n')
f.close()

f = open('ch09_data.txt')
line = f.readline()
print('readline =', line.rstrip())

line = f.readline()
line = line.rstrip()
parts = line.split(',')
print('parts =', parts)
numbers = [int(xx) for xx in parts]
print('numbers =', numbers)

line = f.readline()
line = line.rstrip()
print('line =', line)
print('eval(line) =', eval(line))

line = f.readline()
line = line.rstrip()
print('line =', line)
print('eval(line) =', eval(line))

f.close()
