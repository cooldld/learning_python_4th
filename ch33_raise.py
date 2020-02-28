try:
    raise IndexError('spam')
except IndexError:
    print('except IndexError')
    print('raise with nothing')
    raise
