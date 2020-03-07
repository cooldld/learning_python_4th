print('class c_name, def __get__/__set__/__delete__')
class c_name:
    'name property docs'
    def __get__(self, instance, owner):
        print('c_name.__get__')
        return instance._name
    def __set__(self, instance, value):
        print('c_name.__set__')
        instance._name = value
    def __delete__(self, instance):
        print('c_name.__delete__')
        del instance._name

print()
print('class c_person, name = c_name()')
class c_person:
    def __init__(self, name):
        self._name = name
    name = c_name()

print()
print("bob = c_person('bob smith')")
bob = c_person('bob smith')

print()
print('bob.name =')
print(bob.name)

print()
print("bob.name = 'robert smith'")
bob.name = 'robert smith'

print()
print('bob.name =')
print(bob.name)

print()
print('del bob.name')
del bob.name

print()
print('c_name.__doc__')
print(c_name.__doc__)
