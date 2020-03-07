print('class c_person, def get_name/set_name/del_name')
class c_person:
    def __init__(self, value):
        self._name = value
    def get_name(self):
        print('c_person.get_name')
        return self._name
    def set_name(self, value):
        print('c_person.set_name')
        self._name = value
    def del_name(self):
        print('c_person.del_name')
        del self._name
    print("name = property(get_name, set_name, del_name, 'name property docs')")
    name = property(get_name, set_name, del_name, 'name property docs')

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
