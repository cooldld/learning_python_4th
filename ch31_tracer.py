print('class c_tracer, def __call__')
class c_tracer:
    def __init__(self, func):
        self.num = 0
        self.func = func
    def __call__(self, *args):
        self.num += 1
        print('c_tracer.__call__, num = %s, func.name = %s, args = %s' % (self.num, self.func.__name__, args))
        self.func(*args)

print()
print('@c_tracer')
print('def spam')
@c_tracer
def spam(a, b, c):
    print('spam, a = %s, b = %s, c = %s' % (a, b, c))

print()
print('spam =', spam)

print()
print("spam(1, 2, 3)")
spam(1, 2, 3)
print("spam('x', 'y', 'z')")
spam('x', 'y', 'z')
print("spam(4, 5, 6)")
spam(4, 5, 6)
