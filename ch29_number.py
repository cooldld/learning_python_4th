print('class Number')
class Number:
    def __init__(self, start):
        self.data = start
    def __sub__(self, other):
        return Number(self.data - other)

print('')
print('x = Number(5)')
x = Number(5)
print('y = x - 2')
y = x - 2
print('y.data =', y.data)
