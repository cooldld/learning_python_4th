import struct

#how to use struct
#help(struct)

F = open('ch09_data.struct', 'wb')
data = struct.pack('>i4sh', 7, b'spam', 8)
print('struct.pack, data =', data)
F.write(data)
F.close

F = open('ch09_data.struct', 'rb')
data = F.read()
print('file read, data =', data)
values = struct.unpack('>i4sh', data)
print('struct.unpack, values =', values)
