print('class c_prop_square, def getX/setX')
class c_prop_square:
    def __init__(self, val):
        self.value = val
    def getX(self):
        print('c_prop_square.getX')
        return self.value ** 2
    def setX(self, val):
        print('c_prop_square.setX')
        self.value = val
    print('X = property(getX, setX)')
    X = property(getX, setX)

print()
print('P = c_prop_square(3)')
P = c_prop_square(3)
print('Q = c_prop_square(5)')
Q = c_prop_square(5)

print()
print('P.X =')
print(P.X)

print()
print('P.X = 10')
P.X = 10

print()
print('P.X =')
print(P.X)

print()
print('Q.X =')
print(Q.X)
