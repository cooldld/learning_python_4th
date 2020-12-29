print('class c_myexc(Exception): pass')
class c_myexc(Exception): pass

print()
print("try and raise c_myexc('spam')")
try:
    raise c_myexc('spam')
except c_myexc as x:
    print('exception: c_myexc, type(x) =%s, x = %s, x.args = %s' % (type(x), x, x.args))

'''
TypeError: exceptions must derive from BaseException
raise list('spam')
'''
