class Super:
    def method(self):
        print('in Super.method')
    def delegate(self):
        self.action()
    def action(self): #定义抽象超类的方法
        #assert False, 'action() not defined!'
        raise NotImplementedError('action() not defined!')

class Inheritor(Super):
    pass

class Replacer(Super):
    def method(self):
        print('in Replacer.method')

class Extender(Super):
    def method(self):
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')

class Provider(Super):
    def action(self):
        print('in Provider.action')

print('''
error!!!
NotImplementedError: action() not defined!
Inheritor().action()
''')

if __name__ == '__main__':
    for cs in (Inheritor, Replacer, Extender):
        print('\n' + cs.__name__ + '...')
        cs().method()
    print('\nProvider...')
    x = Provider()
    x.action()
