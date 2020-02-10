D = {'food': 'spam', 'quantity': 4, 'color': 'pink'}

print('dir(D) =', dir(D))
print('D = ', D)
print('D[food] = ', D['food'])

D['quantity'] += 1
print('quantity +=1, D = ', D)

D = {}
D['name'] = 'Bob'
D['job'] = 'dev'
D['age'] = 40
print('D = ', D)

rec = {'name': {'first': 'Bob', 'last': 'Smith'},
    'job': ['dev', 'mgr'],
    'age': 40.5}
print('rec = ', rec)

D = {'b': 2, 'c': 3, 'a': 1}
print('D = ', D)
keys = list(D.keys())
print('list(D.keys()) = ', keys)
keys.sort()
print('keys.sort = ', keys)
for key in keys:
    print(key, '=>', D[key])

D = {'b': 2, 'c': 3, 'a': 1}
print('D = ', D)
for key in sorted(D):
    print(key, '=>', D[key])

if 'b' in D:
    print('b in D')
else:
    print('b not in D')

if 'f' in D:
    print('f in D')
else:
    print('f not in D')

value = D.get('x', -1)
print('D.get(x, -1) =', value)

value = D['x'] if 'x' in D else -2
print('value =', value)
