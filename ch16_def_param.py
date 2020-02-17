def list_change(l1):
    l1[1] = 'aaa'


L = [1, 2, 3]
print('L =', L)

list_change(L)
print('list_change(L) =', L)
