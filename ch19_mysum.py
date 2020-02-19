def mysum0(L):
    print('L =', L)
    if not L:
        return 0
    else:
        return L[0] + mysum0(L[1:])

print('mysum0([1, 2, 3, 4, 5]) =', mysum0([1, 2, 3, 4, 5]))

def mysum1(L):
    return 0 if not L else L[0] + mysum1(L[1:])
print('mysum1([1, 2, 3, 4, 5]) =', mysum1([1, 2, 3, 4, 5]))

def mysum2(L):
    return L[0] if len(L) == 1 else L[0] + mysum2(L[1:])
print('mysum2([1, 2, 3, 4, 5]) =', mysum2([1, 2, 3, 4, 5]))

def mysum3(L):
    first, *rest = L
    return first if not rest else first + mysum3(rest)
print('mysum3([1, 2, 3, 4, 5]) =', mysum3([1, 2, 3, 4, 5]))
print("mysum3('spam') =", mysum3('spam'))
