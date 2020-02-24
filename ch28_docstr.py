'I am: docstr.__doc__'

def func(args):
    'I am: docstr.func.__doc__'
    pass

class spam:
    'I am: spam.__doc__ or docstr.spam.__doc__'
    def method(self, arg):
        'I am: spam.method.__doc__ or docstr.spam.method.__doc__'
        pass

if __name__ == '__main__':
    print('self test')
    import ch28_docstr as docstr
    print('docstr.__doc__ =', docstr.__doc__)
    print('docstr.func.__doc__ =', docstr.func.__doc__)
    print('docstr.spam.__doc__ =', docstr.spam.__doc__)
    print('docstr.spam.method.__doc__ =', docstr.spam.method.__doc__)
    print('call help(docstr)')
    help(docstr)
