#create a dictionary
D = {}
print('dir(D) =', dir(D))
print('D =', D)

D = {'spam': 2, 'eggs': 3}
print('D =', D)
print("D['eggs'] =", D['eggs'])
print("'eggs' in D =", 'eggs' in D)

D = {'food': {'ham': 1, 'eggs': 2}}
print('D =', D)
print("D['food']['eggs'] =", D['food']['eggs'])

D = dict.fromkeys(['a', 'b'])
print("dict.fromkeys(['a', 'b']) =", D)
D = dict.fromkeys(['a', 'b'], 0)
print("dict.fromkeys(['a', 'b'], 0) =", D)
print('D.values() =', D.values())

D = dict(zip(['a', 'b'], [1, 2]))
print("dict(zip(['a', 'b'], [1, 2])) =", D)

L = list(zip(['a', 'b'], [1, 2]))
print("list(zip(['a', 'b'], [1, 2])) =", L)

D = dict([('a', 'b'), (1, 2)])
print("dict([('a', 'b'), (1, 2)]) =", D)

D = dict(name='Bob', age=42)
print("dict(name='Bob', age=42) =", D)
print('D.keys() =', D.keys())
print('list(D.keys()) =', list(D.keys()))
print('D.values() =', D.values())
print('list(D.values()) =', list(D.values()))
print('D.items() =', D.items())
print('list(D.items()) =', list(D.items()))
print('D.copy() =', D.copy())
print("D.get('name') =", D.get('name'))
print("D.get('namexx') =", D.get('namexx'))
print("D.get('namexx', 'nobody') =", D.get('namexx', 'nobody'))

D1 = {'spam': 2, 'eggs': 3}
print('D =', D)
print('D1 =', D1)
D.update(D1)
print('D.update(D1) =', D)

print("D.pop('spam') =", D.pop('spam'))
print('D =', D)
print('len(D) =', len(D))

D['spam'] = 'hello'
print("D['spam'] = 'hello', D =", D)
D['eggs'] = 'world'
print("D['eggs'] = 'world', D =", D)

del D['eggs']
print("del D['eggs'] =", D)

print('D.keys() & D1.keys() =', D.keys() & D1.keys())

D = {x: x * 2 for x in range(10)}
print('{x: x * 2 for x in range(10)} =', D)
print('D[9] =', D[9])
D['food'] = 'spam'
for x in D:
    print(x, ':', D[x])

D = {'spam': 2, 'eggs': 3, 'hello': 'xxx'}
print('D =', D)
for k in sorted(D): print(k, ':', D[k])
