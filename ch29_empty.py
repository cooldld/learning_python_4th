print('class empty, def __getattr__')
class empty:
    def __getattr__(self, attrname):
        print('call __getattr__, attrname =', attrname)
        if attrname == 'age':
            return 40
        else:
            raise AttributeError(attrname)

print()
print('x = empty()')
x = empty()
print('x.age =', x.age)

'''
error!!!
AttributeError: height
print('x.height =', x.height)
'''
