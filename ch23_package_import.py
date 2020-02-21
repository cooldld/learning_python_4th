print('import ch23_dir1.ch23_dir2')
import ch23_dir1.ch23_dir2

print('')
print('import ch23_dir1.ch23_dir2.mod')
import ch23_dir1.ch23_dir2.mod

print('')
print('import ch23_dir1.ch23_dir2.mod')
import ch23_dir1.ch23_dir2.mod

print('')
print('ch23_dir1 =', ch23_dir1)
print('ch23_dir1.x =', ch23_dir1.x)
print('ch23_dir1.ch23_dir2 =', ch23_dir1.ch23_dir2)
print('ch23_dir1.ch23_dir2.y =', ch23_dir1.ch23_dir2.y)
print('ch23_dir1.ch23_dir2.mod =', ch23_dir1.ch23_dir2.mod)
print('ch23_dir1.ch23_dir2.mod.z =', ch23_dir1.ch23_dir2.mod.z)

#模块包的相对导入
print('')
print('ch23_dir1.ch23_dir2.mod.string =', ch23_dir1.ch23_dir2.mod.string)
print('import ch23_dir1.ch23_dir2.mod2')
import ch23_dir1.ch23_dir2.mod2
print('ch23_dir1.ch23_dir2.mod2.string =', ch23_dir1.ch23_dir2.mod2.string)

print('')
print('from imp import reload')
from imp import reload

print('')
print('reload(ch23_dir1.ch23_dir2)')
reload(ch23_dir1.ch23_dir2)

print('')
print('reload(ch23_dir1)')
reload(ch23_dir1)

print('')
print('reload(ch23_dir1.ch23_dir2)')
reload(ch23_dir1.ch23_dir2)

print('')
print('from ch23_dir1.ch23_dir2 import mod')
from ch23_dir1.ch23_dir2 import mod
print('mod.z =', mod.z)

print('')
print('from ch23_dir1.ch23_dir2.mod import z')
from ch23_dir1.ch23_dir2.mod import z
print('z =', z)

print('')
print('import ch23_dir1.ch23_dir2.mod as modxx')
import ch23_dir1.ch23_dir2.mod as modxx
print('modxx.z =', modxx.z)
