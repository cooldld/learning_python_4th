print('class c_descriptor, def __get__')
class c_descriptor:
    def __get__(self, instance, owner):
        print('c_descriptor.__get__')
        print('self =', self)
        print('instance =', instance)
        print('owner =', owner)

print()
print('class c_subject')
class c_subject:
    print('attr = c_descriptor()')
    attr = c_descriptor()

print()
print('x = c_subject()')
x = c_subject()

print()
print('x.attr')
x.attr

print()
print('c_subject.attr')
c_subject.attr
