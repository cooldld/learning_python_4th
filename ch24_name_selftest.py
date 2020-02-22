print('I am:', __name__)

def minmax(compare, *args):
    res = args[0]
    for arg in args[1:]:
        if compare(arg, res):
            res = arg
    return res

def lessthan(x, y): return x < y
def grtrthan(x, y): return x > y

#self test code
if __name__ == '__main__':
    print('call minmax(lessthan, 4, 2, 1, 5, 6, 3)')
    print(minmax(lessthan, 4, 2, 1, 5, 6, 3))
    print('call minmax(grtrthan, 4, 2, 1, 5, 6, 3)')
    print(minmax(grtrthan, 4, 2, 1, 5, 6, 3))
