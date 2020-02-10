class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

bob = Worker('Bob Smith', 50000)
sue = Worker('Sue Jones', 60000)

print("dir(bob) =", dir(bob))
print("help(bob.giveRaise) =", help(bob.giveRaise))

print("bob =", bob)
print("sue =", sue)

print("bob.name =", bob.name)
print("sue.name =", sue.name)

print("bob.lastName() =", bob.lastName())
print("sue.lastName() =", sue.lastName())

sue.giveRaise(.10)
print("sue.giveRaise(.10), sue.pay =", sue.pay)
