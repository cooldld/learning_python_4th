print('class Callback, def __call__')
class Callback:
    def __init__(self, color):
        self.color = color
    def __call__(self):
        print('__call__, color =', self.color)

print()
print("cb1 = Callback('blue')")
cb1 = Callback('blue')
print("cb2 = Callback('green')")
cb2 = Callback('green')

print('cb1()')
cb1()
print('cb2()')
cb2()
