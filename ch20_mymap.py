s1 = 'abc'
s2 = 'xyz123'
print('s1 = %s, s2 = %s' % (s1, s2))
print('list(zip(s1, s2)) =', list(zip(s1, s2)))

L = list(zip([-2, -1, 0, 1, 2]))
print('list(zip([-2, -1, 0, 1, 2])) =', L)

L = list(zip([1, 2, 3], [10, 20, 30, 40]))
print('list(zip([1, 2, 3], [10, 20, 30, 40])) =', L)

L = list(map(abs, [-2, -1, 0, 1, 2]))
print('list(map(abs, [-2, -1, 0, 1, 2])) =', L)

L = list(map(pow, [1, 2, 3], [2, 3, 4, 5]))
print('list(map(pow, [1, 2, 3], [2, 3, 4, 5])) =', L)

print('')
print('def mymap(func, *seqs), many ways')
print('')

print('#work alike with zip')

'''
def mymap(func, *seqs):
    res = []
    for args in zip(*seqs):
        res.append(func(*args))
    return res
'''

def mymap(func, *seqs):
    res = []
    for args in zip(*seqs):
        res.append(func(*args))
    return res

L = list(mymap(abs, [-2, -1, 0, 1, 2]))
print('list(mymap(abs, [-2, -1, 0, 1, 2])) =', L)
L = list(mymap(pow, [1, 2, 3], [2, 3, 4, 5]))
print('list(mymap(pow, [1, 2, 3], [2, 3, 4, 5])) =', L)

print('')
print('#using a list comprehension')

'''
def mymap(func, *seqs):
    return [func(*args) for args in zip(*seqs)]
'''

def mymap(func, *seqs):
    return [func(*args) for args in zip(*seqs)]

L = list(mymap(abs, [-2, -1, 0, 1, 2]))
print('list(mymap(abs, [-2, -1, 0, 1, 2])) =', L)
L = list(mymap(pow, [1, 2, 3], [2, 3, 4, 5]))
print('list(mymap(pow, [1, 2, 3], [2, 3, 4, 5])) =', L)

print('')
print('#using generators: yield')

'''
def mymap(func, *seqs):
    for args in zip(*seqs):
        yield func(*args)
'''

def mymap(func, *seqs):
    for args in zip(*seqs):
        yield func(*args)

L = list(mymap(abs, [-2, -1, 0, 1, 2]))
print('list(mymap(abs, [-2, -1, 0, 1, 2])) =', L)
L = list(mymap(pow, [1, 2, 3], [2, 3, 4, 5]))
print('list(mymap(pow, [1, 2, 3], [2, 3, 4, 5])) =', L)

print('')
print('#using generators: (...)')

'''
def mymap(func, *seqs):
    return (func(*args) for args in zip(*seqs))
'''

def mymap(func, *seqs):
    return (func(*args) for args in zip(*seqs))

L = list(mymap(abs, [-2, -1, 0, 1, 2]))
print('list(mymap(abs, [-2, -1, 0, 1, 2])) =', L)
L = list(mymap(pow, [1, 2, 3], [2, 3, 4, 5]))
print('list(mymap(pow, [1, 2, 3], [2, 3, 4, 5])) =', L)
