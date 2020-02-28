print('class c_format_error(Exception), def __init__')
class c_format_error(Exception):
    def __init__(self, line, file):
        self.line = line
        self.file = file

print()
print("try and raise c_format_error(42, 'spam.txt')")
try:
    raise c_format_error(42, 'spam.txt')
except c_format_error as x:
    print('except c_format_error, x.line = %s, x.file = %s' % (x.line, x.file))

print()
print("try and raise c_format_error(42, 'spam.txt')")
try:
    raise c_format_error(42, 'spam.txt')
except c_format_error as x:
    print('except c_format_error, x.args[0] = %s, x.args[1] = %s' % (x.args[0], x.args[1]))
