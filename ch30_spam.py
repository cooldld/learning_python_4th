print('class c_spam, def bound_func/unbound_func')
class c_spam:
    def bound_func(self, msg):
        print('c_spam.bound_func(), msg =', msg)
    def unbound_func(msg):
        print('c_spam.unbound_func(), msg =', msg)

print()
print('obj = c_spam()')
obj = c_spam()
print("obj.bound_func('hello')")
obj.bound_func('hello')

'''
error!!!
TypeError: unbound_func() takes 1 positional argument but 2 were given
obj.unbound_func('hello')
'''

print("c_spam.unbound_func('hello unbound')")
c_spam.unbound_func('hello unbound')

print()
print('t = c_spam.bound_func')
t = c_spam.bound_func
print('t =', t)
print("t(obj, 'hello bound')")
t(obj, 'hello bound')

print()
print('t = c_spam.unbound_func')
t = c_spam.unbound_func
print('t =', t)
print("t('hello unbound')")
t('hello unbound')

'''
error!!!
TypeError: unbound_func() takes 1 positional argument but 2 were given
t(obj, 'hello bound')
'''
