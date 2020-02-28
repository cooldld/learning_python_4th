print('class c_format_error(Exception), def __init__')
class c_format_error(Exception):
    log_file = 'ch34_format_error.log'
    def __init__(self, line, file):
        self.line = line
        self.file = file
    def log_error(self):
        print('open file', self.log_file)
        log = open(self.log_file, 'a')
        print('c_format_error.log_error', self.file, self.line, file = log)
        log.close()

print()
print("try and raise c_format_error(42, 'spam.txt')")
try:
    raise c_format_error(42, 'spam.txt')
except c_format_error as x:
    print('except c_format_error, x.log_error()')
    x.log_error()
