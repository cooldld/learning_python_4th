print('from ch30_streams import Processor')
from ch30_streams import Processor

print()
print('class Uppercase(Processor)')
class Uppercase(Processor):
    def converter(self, data):
        #print('Uppercase.converter, data =', data)
        return data.upper()

print()
print('class c_html_write')
class c_html_write:
    def write(self, line):
        print('<>%s</>' % line.rstrip())

if __name__ == '__main__':
    print()
    print('self test')
    import sys
    print("obj = Uppercase(open('ch30_streams.py'), sys.stdout)")
    obj = Uppercase(open('ch30_streams.py'), sys.stdout)
    print('obj.process()')
    obj.process()
    print()
    print("obj = Uppercase(open('ch30_streams.py'), c_html_write())")
    obj = Uppercase(open('ch30_streams.py'), c_html_write())
    print('obj.process()')
    obj.process()
