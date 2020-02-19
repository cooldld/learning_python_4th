from functools import reduce

L = [1, 2, 3, 4]
print('L =', L, '\n')

ret = reduce((lambda x, y: x + y), L)
print('reduce((lambda x, y: x + y), L) = ', ret)

ret = reduce((lambda x, y: x * y), L)
print('reduce((lambda x, y: x * y), L) = ', ret)

print('\ndef myreduce(func, seq)')
def myreduce(func, seq):
    tally = seq[0]
    for next in seq[1:]:
        tally = func(tally, next)
    return tally

ret = myreduce((lambda x, y: x + y), L)
print('myreduce((lambda x, y: x + y), L) = ', ret)

ret = myreduce((lambda x, y: x * y), L)
print('myreduce((lambda x, y: x * y), L) = ', ret)

