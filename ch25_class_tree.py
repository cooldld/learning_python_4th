print('class C2')
class C2: pass

print('class C3')
class C3: pass

print('class C1(C2, C3)')
class C1(C2, C3): pass

I1 = C1()
I2 = C2()
I3 = C3()

print('I1 = C1(), I1 =', I1)
#print('dir(I1) =', dir(I1))
print('I2 = C2(), I2 =', I2)
print('I3 = C3(), I3 =', I3)
