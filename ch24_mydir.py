'''
ch24_mydir.py: a module that lists the namespaces of other modules
'''

seplen = 60
sepchr = '-'

def listing(module, verbose = True):
    print('listing all names of module', module.__name__)
    sepline = sepchr * seplen
    if verbose:
        print(sepline)
        print('name = %s, file = %s' % (module.__name__, module.__file__))

    count = 0
    for attr in module.__dict__:
        print('%02d) %s :' % (count, attr), end = ' ')
        if attr.startswith('__'):
            print('<built-in name>')
        else:
            print(getattr(module, attr))
        count += 1

    if verbose:
        print(module.__name__, 'has %d names', count)
        print(sepline)

if __name__ == '__main__':
    print(__name__, 'self test')
    print('import ch24_mydir')
    import ch24_mydir
    print('listing(ch24_mydir)')
    listing(ch24_mydir)
