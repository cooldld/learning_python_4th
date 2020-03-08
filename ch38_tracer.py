print('class c_tracer, def __init__/__call__')
class c_tracer:
    def __init__(self, func):
        print('c_tracer.__init__')
        self.calls = 0
        self.func = func
    def __call__(self, *args):
        print('c_tracer.__call__')
        self.calls += 1
        print('self.calls =', self.calls)
        print('self.func')
        self.func(*args)

print()
print('@c_tracer')
print('def spam(a, b, c)')
@c_tracer
def spam(a, b, c):
    print('spam, a + b + c =', a + b + c)

print()
print('spam =', spam)

print()
print('spam(1, 2, 3)')
spam(1, 2, 3)

print()
print("spam('a', 'b', 'c')")
spam('a', 'b', 'c')
