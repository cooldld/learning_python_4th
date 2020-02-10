L = [1, 2, 3, 4]

print('L =', L)
print('type(L) =', type(L))

if type(L) == type([]):
    print('type(L) is type([])')

if type(L) == list:
    print('type(L) is list')

if isinstance(L, list):
    print('L isinstance list')
