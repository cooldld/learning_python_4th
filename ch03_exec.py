title = 'hello'
print('title =', title)

print('exec ch03_myfile.py')
exec(open('ch03_myfile.py').read())

print('#title is instead by ch03_myfile.py')
print('title =', title)
