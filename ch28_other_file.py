print('import ch28_many_names as many_names')
import ch28_many_names as many_names

print('other_file, set x to 66')
x = 66

print('x =', x)
print('many_names.x =', many_names.x)

print('many_names.f()')
many_names.f()

print('many_names.g()')
many_names.g()

print('many_names.C.x =', many_names.C.x)

print('I = many_names.C()')
I = many_names.C()
print('I.x =', I.x)
print('call I.m()')
I.m()
print('I.x =', I.x)
