print('class lt_gt, def __gt__/__lt__')
class lt_gt:
    data = 'spam'
    def __gt__(self, other):
        return self.data > other
    def __lt__(self, other):
        return self.data < other

print('x = lt_gt()')
x = lt_gt()

print("x > 'ham' =", x > 'ham')
print("x < 'ham' =", x < 'ham')
