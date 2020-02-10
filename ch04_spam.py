str = 'Spam'

print(len(str))

print(str[0])
print(str[1])

print(str[-1])
print(str[len(str)-1])

print(str[-2])

#slice of str from offsets 1 through 2 (not 3)
print(str[1:3])

print('str =', str)
print('str[1:] =', str[1:])
print('str[0:3] =', str[0:3])
print('str[:3] =', str[:3])
print('str[:-1] =', str[:-1])
print('str[:] =', str[:])

print('str + xyz =', str + 'xyz')
print('str * 3 =', str * 3)

print('str find pa =', str.find('pa'))
print('str replace pa by XYZ =', str.replace('pa', 'XYZ'))
print('str.upper =', str.upper())
print('str.isalpha =', str.isalpha())

line = 'aaa,bbb,cc,dd'
print('line =', line)
print('line.split =', line.split(','))

line1 = 'aaa,bbb,cc,dd\n'
print('line1 =', line1)
print('line1.rstrip =', line1.rstrip())

#format string
print('%s, eggs, and %s' % ('spam', 'SPAM!'))
print('{0}, eggs, and {1}'.format('spam', 'SPAM!'))

print('dir(str) =', dir(str))

print(ord(str[0]))

str1 = 'a\nb'
print(str1)
str2 = r'a\nb'
print(str2)
