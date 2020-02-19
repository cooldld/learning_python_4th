L = [1, 2, 3, 4]
print('L =', L)

print('def inc(x): return x + 10')
def inc(x): return x + 10

result = map(inc, L)
print('map(inc, L) =', result)
print('list(map(inc, L)) =', list(result))

print('list(map((lambda x: x + 10), L)) =', list(map((lambda x: x + 10), L)))

print('\ndef mymap(func, seq)')
def mymap(func, seq):
    res = []
    for x in seq: res.append(func(x))
    return res

print('mymap(inc, L) =', mymap(inc, L))
print('mymap((lambda x: x + 10), L) =', mymap((lambda x: x + 10), L))

print('')
print('pow(3, 4) =', pow(3, 4))
print('list(map(pow, [2, 3, 4], [1, 2, 3])) =', list(map(pow, [2, 3, 4], [1, 2, 3])))
