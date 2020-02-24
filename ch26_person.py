print('''
通过一个空类产生的实例来记录信息
class Person1: pass

person_a = Person1()
person_a.name = 'bob'
person_a.job = 'trainer'
''')

print('class Person2')
class Person2:
    def __init__(self, name, job):
        self.name = name
        self.job = job
    def info(self):
        return (self.name, self.job)

print("person_b = Person2('mel', 'trainer')")
person_b = Person2('mel', 'trainer')
print("person_c = Person2('vls', 'developer')")
person_c = Person2('vls', 'developer')

print('person_b.name = %s, person_c.name = %s' % (person_b.name, person_c.name))
