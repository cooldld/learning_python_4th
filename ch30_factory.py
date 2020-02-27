print('def factory(class_type, *args, **kw_args)')
def factory(class_type, *args, **kw_args):
    return class_type(*args, **kw_args)

print()
print('class c_spam, def doit')
class c_spam:
    def doit(self, msg): print('c_spam.doit(), msg =', msg)

print()
print('class c_person')
class c_person:
    def __init__(self, name, job):
        self.name = name
        self.job = job

print()
print('spam_obj = factory(c_spam)')
spam_obj = factory(c_spam)
print("spam_obj.doit('hello')")
spam_obj.doit('hello')

print()
print("person_obj = factory(c_person, 'bob', 'chef')")
person_obj = factory(c_person, 'bob', 'chef')
print('person_obj, name = %s, job = %s' % (person_obj.name, person_obj.job))
