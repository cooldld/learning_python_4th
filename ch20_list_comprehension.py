L = [ord(x) for x in 'spam']
print("[ord(x) for x in 'spam'] =", L)

L = [x ** 2 for x in range(10)]
print('[x ** 2 for x in range(10)] =', L)

L = list(map((lambda x: x ** 2), range(10)))
print('list(map((lambda x: x ** 2), range(10))) =', L)

L = [x for x in range(5) if x % 2 == 0]
print('[x for x in range(5) if x % 2 == 0] =', L)

L = list(map((lambda x: x ** 2), filter((lambda x: x % 2 == 0), range(10))))
print('list(map((lambda x: x ** 2), filter((lambda x: x % 2 == 0), range(10)))) =', L)

print('')
L = [x + y for x in [0, 1, 2] for y in [10, 20, 30]]
print('[x + y for x in [0, 1, 2] for y in [10, 20, 30]] =', L)

L = [x + y for x in 'abc' for y in '12']
print("[x + y for x in 'abc' for y in '12'] =", L)

print('')
listoftuple = [('bob', 35, 'mgr'), ('mel', 40, 'dev')]
print('listoftuple =', listoftuple)
L = [age for (name, age, job) in listoftuple]
print('[age for (name, age, job) in listoftuple] =', L)
L = list(map((lambda row: row[1]), listoftuple))
print('list(map((lambda row: row[1]), listoftuple)) =', L)

'''
error!!!
#2.6 only
L = list(map((lambda (name, age, job): age), listoftuple))
'''
