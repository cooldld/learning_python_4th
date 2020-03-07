print('class c_person, def get_name/set_name/del_name')
class c_person:
    def __init__(self, value):
        self._name = value

    @property
    def name(self):
        'name property docs'
        print('c_person, name = property(name)')
        return self._name

    @name.setter
    def name(self, value):
        print('c_person, name = name.setter(name)')
        self._name = value

    @name.deleter
    def name(self):
        print('c_person, name = name.deleter(name)')
        del self._name

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
print('c_person.name.__doc__')
print(c_person.name.__doc__)
