print('class c_list(list)')
class c_list(list):
    def __getitem__(self, offset):
        print('c_list.__getitem__(), offset =', offset)
        return list.__getitem__(self, offset - 1)

if __name__ == '__main__':
    print()
    print('self test')
    print("x = list('abc')")
    x = list('abc')
    print('x =', x)
    print("y = c_list('abc')")
    y = c_list('abc')
    print('y =', y)

    print()
    print('x[0] =', x[0])
    print('y[0] =', y[0])
    print('x[2] =', x[2])
    print('y[2] =', y[2])

    print()
    print("x.append('spam')")
    x.append('spam')
    print('x =', x)
    print("y.append('spam')")
    y.append('spam')
    print('y =', y)

    print()
    print('x.reverse()')
    x.reverse()
    print('x =', x)
    print('y.reverse()')
    y.reverse()
    print('y =', y)
