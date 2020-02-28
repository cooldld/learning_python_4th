print('class c_bad(Exception): pass')
class c_bad(Exception): pass

print()
try:
    print('raise c_bad()')
    raise c_bad()
except c_bad:
    print('exception: c_bad')
