print('class Employee')
class Employee:
    def __init__(self, name, salary=0):
        print('Employee, __init__, name = %s, salary = %s' % (name, salary))
        self.name = name
        self.salary = salary
    def give_raise(self, percent):
        self.salary = self.salary + (self.salary * percent)
        print('Employee, give_raise, percent = %s, salary = %s' % (percent, self.salary))
    def work(self):
        print('Employee, work, name =', self.name)
    def __repr__(self):
        return 'Employee, name = %s, salary = %s' % (self.name, self.salary)

print('')
print('class Chef(Employee)')
class Chef(Employee):
    def __init__(self, name):
        print('Chef, __init__, name =', name)
        Employee.__init__(self, name, 50000)
    def work(self):
        print('Chef, work, name =', self.name)

print('')
print('class Server(Employee)')
class Server(Employee):
    def __init__(self, name):
        print('Server, __init__, name =', name)
        Employee.__init__(self, name, 40000)
    def work(self):
        print('Server, work, name =', self.name)

print('')
print('class Pizza_robot(Chef)')
class Pizza_robot(Chef):
    def __init__(self, name):
        print('Pizza_robot, __init__, name =', name)
        Chef.__init__(self, name)
    def work(self):
        print('Pizza_robot, work, name =', self.name)

if __name__ == '__main__':
    print('')
    print('self test')
    print("bob = Pizza_robot('bob')")
    bob = Pizza_robot('bob')
    print('bob =', bob)
    print('bob.work()')
    bob.work()
    print('bob.give_raise(0.20)')
    bob.give_raise(0.20)
    print('bob =', bob)
    print()

    print('for cs in Employee, Chef, Server, Pizza_robot')
    for cs in Employee, Chef, Server, Pizza_robot:
        print('cs =', cs)
        print('cs.__name__ =', cs.__name__)
        print('obj = cs(cs.__name__)')
        obj = cs(cs.__name__)
        print('obj.work()')
        obj.work()
