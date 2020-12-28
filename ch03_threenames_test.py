import ch03_threenames
print(ch03_threenames.b, ch03_threenames.c)

ch03_threenames.a[0] = 'x'
ch03_threenames.b = 'hello'

from ch03_threenames import a, b, c
print(a, b, c)

a[0] = 'y'
b = 'world'
print(ch03_threenames.a, ch03_threenames.b, ch03_threenames.c)

print(dir(ch03_threenames))
