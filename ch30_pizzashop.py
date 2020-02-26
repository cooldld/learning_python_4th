print('from ch30_employees import Pizza_robot, Server')
from ch30_employees import Pizza_robot, Server

print()
print('class Customer')
class Customer:
    def __init__(self, name):
        self.name = name
    def order(self, server):
        print('Customer, order, name = %s, server = %s' % (self.name, server.name))
    def pay(self, server):
        print('Customer, pay, name = %s, server = %s' % (self.name, server.name))

print()
print('class Oven')
class Oven:
    def bake(self):
        print('Oven, bakes')

print()
print('class Pizza_shop')
class Pizza_shop:
    def __init__(self):
        self.server = Server('Pat')
        self.chef = Pizza_robot('Bob')
        self.oven = Oven()
    def order(self, name):
        print('Pizza_shop, order, name =', name)
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)

if __name__ == '__main__':
    print()
    print('self test')
    scene = Pizza_shop()
    scene.order('Jack')
    print('...')
    scene.order('Shaggy')
