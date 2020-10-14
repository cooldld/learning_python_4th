import struct

struct_file = 'ch09_struct.data'
print('struct_file =', struct_file)

F = open(struct_file, 'wb')
data = struct.pack('>i4sh', 7, b'spam', 8)
print('struct.pack, data =', data)
F.write(data)
F.close

F = open(struct_file, 'rb')
data = F.read()
print('file read, data =', data)
values = struct.unpack('>i4sh', data)
print('struct.unpack, values =', values)
