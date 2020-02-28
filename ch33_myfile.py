print("with open('ch33_raise_from.py') as myfile")

print()
with open('ch33_raise_from.py') as myfile:
    for line in myfile:
        print(line.rstrip())

print()
print('MUST not myfile.close()')
