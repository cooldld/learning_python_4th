s = 'spammy'
print('s =', s)

s = s[:3] + 'xx' + s[5:]
print("s[:3] + 'xx' + s[5:] =", s)

s = 'spammy'
s = s.replace('mm', 'xx')
print("s.replace('mm', 'xx') =", s)

s = 'aa$bb$cc$dd'
print('s =', s)
s = s.replace('$', 'SPAM')
print("s.replace('$', 'SPAM') =", s)

s = 'xxxxSPAMxxxxSPAM'
print('s =', s)
s = s.replace('SPAM', 'EGGS')
print("s.replace('SPAM', 'EGGS') =", s)

s = 'xxxxSPAMxxxxSPAM'
#print('s =', s)
s = s.replace('SPAM', 'EGGS', 1)
print("s.replace('SPAM', 'EGGS', 1) =", s)

s = 'xxxxSPAMxxxxSPAM'
where = s.find('SPAM')
s = s[:where] + 'EGGS' + s[(where+4):]
print("s[:where] + 'EGGS' + s[(where+4):] =", s)

s = 'spammy'
print('s =', s)
l = list(s)
print('list(s) =', l)
l[3] = 'x'
l[4] = 'x'
print('l[3] = l[4] = x, list =', l)
s = ''.join(l)
print("''.join(l) =", s)
s = ', '.join(l)
print("', '.join(l) =", s)

s = 'aaa bbb ccc'
print('s =', s)
s = s.split()
print('s.split() =', s)

s = 'aaa,bbb,ccc'
print('s =', s)
s = s.split(',')
print("s.split(',') =", s)

s = 'aaaSPAMbbbSPAMccc'
print('s =', s)
s = s.split('SPAM')
print("s.split('SPAM') =", s)

s = 'The knights who say Ni!\n'
print('s =', s)
print("s.rstrip() =", s.rstrip())
print("s.upper() =", s.upper())
print("s.isalpha() =", s.isalpha())
print("s.endswith('Ni!\n') =", s.endswith('Ni!\n'))
print("s.startswith('The') =", s.startswith('The'))
print("s.find('Ni') =", s.find('Ni'))
print("'Ni' in s =", 'Ni' in s)
