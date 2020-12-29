print('class accesscontrol, def __setattr__')
class accesscontrol:
    def __setattr__(self, attr, value):
        print('call __setattr__, attr = %s, value = %s' % (attr, value))
        if attr == 'age':
            self.__dict__[attr] = value
        else:
            raise AttributeError(attr + ' not allowed')

print()
print('x = accesscontrol()')
x = accesscontrol()
print('dir(x) =', dir(x))

print()
print('x.age = 40')
x.age = 40
print('dir(x) =', dir(x))

'''
error!!!
AttributeError: name not allowed
x.name = 'spam'
'''
