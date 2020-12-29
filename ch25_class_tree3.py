class C2: pass

class C3: pass

class C1(C2, C3):
    #def __init__(self, who = None):
    def __init__(self, who):
        self.name = who

'''
error!!!
TypeError: __init__() missing 1 required positional argument: 'who'
I1 = C1()
'''

print("I1 = C1('bob')")
I1 = C1('bob')
print('I1.name =', I1.name)

print('')
print("I2 = C1('tom')")
I2 = C1('tom')
print('I2.name =', I2.name)
