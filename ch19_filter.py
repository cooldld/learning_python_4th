L = list(range(-5, 5))
print('list(range(-5, 5)) =', L)

L = list(filter((lambda x: x > 0), L))
print('list(filter((lambda x: x > 0), L)) =', L)
