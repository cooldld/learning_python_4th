print('def count(a_class)')
def count(a_class):
    a_class.num = 0
    return a_class()

print()
print('class c_spam: pass')
class c_spam: pass
print('c_spam =', c_spam)

print()
print('@count')
print('class c_spam: pass')
@count
class c_spam: pass
print('c_spam =', c_spam)
