print('class c_spam, use classmethod')
class c_spam:
    num = 0
    def __init__(self):
        c_spam.num += 1
    def print_num(cls):
        print('c_spam.print_num, cls = %s, num =%s' % (cls, c_spam.num))
    print_num = classmethod(print_num)

print()
print('a = c_spam()')
a = c_spam()
print('b = c_spam()')
b = c_spam()
print('c = c_spam()')
c = c_spam()

print()
print('c_spam.print_num()')
c_spam.print_num()

print()
print('a.print_num()')
a.print_num()

print()
print('class c_other(c_spam): pass')
class c_other(c_spam): pass

print()
print('c_other.print_num()')
c_other.print_num()
