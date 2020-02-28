print('class c_trace_block, def __enter__/__exit__')
class c_trace_block:
    def message(self, arg):
        print('c_trace_block.message, arg =', arg)
    def __enter__(self):
        print('c_trace_block.__enter__')
        return self
    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            print('c_trace_block.__exit__, no exception')
        else:
            print('c_trace_block.__exit__, exc_type = %s, exc_value = %s, exc_tb = %s' % (exc_type, exc_value, exc_tb))
            return False
            #return True

print()
print('with c_trace_block() as action')
with c_trace_block() as action:
    print('action =', action)
    action.message('test 1')
    print('test 1, block finish')

print()
print('with c_trace_block() as action')
with c_trace_block() as action:
    print('action =', action)
    action.message('test 2')
    print('test 2, raise TypeError')
    raise TypeError
    print('test 2, block finish')

print()
print("if __exit__ return True, can run here")
print('c_trace_block finish')
