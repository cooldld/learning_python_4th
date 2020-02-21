print('#list comprehension')
L = [x * x for x in range(10)]
print('[x * x for x in range(10)] =', L)
L = [x * x for x in range(10) if x % 2 == 0]
print('[x * x for x in range(10) if x % 2 == 0] =', L)
L = [x + y for x  in [1, 2, 3] for y in [100, 200, 300]]
print('[x + y for x  in [1, 2, 3] for y in [100, 200, 300]] =', L)

print('')
print('#generator expression')
G = (x * x for x in range(10))
print('(x * x for x in range(10)) =', G)
G = (x * x for x in range(10) if x % 2 == 0)
print('(x * x for x in range(10) if x % 2 == 0) =', G)

print('')
print('#set comprehension')
S = {x * x for x in range(10)}
print('{x * x for x in range(10)} =', S)
S = {x * x for x in range(10) if x % 2 == 0}
print('{x * x for x in range(10) if x % 2 == 0} =', S)
S = {x + y for x  in [1, 2, 3] for y in [100, 200, 300]}
print('{x + y for x  in [1, 2, 3] for y in [100, 200, 300]} =', S)
S = {x + y for x  in [1, 2, 3] for y in [1, 2, 3]}
print('{x + y for x  in [1, 2, 3] for y in [1, 2, 3]} =', S)

print('')
print('#dict comprehension')
D = {x: x * x for x in range(10)}
print('{x: x * x for x in range(10)} =', D)
D = {x: x * x for x in range(10) if x % 2 == 0}
print('{x: x * x for x in range(10) if x % 2 == 0} =', D)
D = {x: y for x  in [1, 2, 3] for y in [100, 200, 300]}
print('{x: y for x  in [1, 2, 3] for y in [100, 200, 300]} =', D)
