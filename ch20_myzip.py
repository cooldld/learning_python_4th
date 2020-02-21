s1, s2 = 'abc', 'xyz123'
print('s1 = %s, s2 = %s' % (s1, s2))

print('''
def myzip(*seqs):
    seqs = [list(s) for s in seqs]
    res = []
    while all(seqs):
        res.append(tuple(s.pop(0) for s in seqs))
    return res
''')
def myzip(*seqs):
    seqs = [list(s) for s in seqs]
    res = []
    while all(seqs):
        res.append(tuple(s.pop(0) for s in seqs))
    return res

print('myzip(s1, s2) =', myzip(s1, s2))

print('''
def myzip_pad(*seqs, pad=None):
    seqs = [list(s) for s in seqs]
    res = []
    while any(seqs):
        res.append(tuple((s.pop(0) if s else pad) for s in seqs))
    return res
''')
def myzip_pad(*seqs, pad=None):
    seqs = [list(s) for s in seqs]
    res = []
    while any(seqs):
        res.append(tuple((s.pop(0) if s else pad) for s in seqs))
    return res

print('myzip_pad(s1, s2) =', myzip_pad(s1, s2))
print("myzip_pad(s1, s2, pad='null') =", myzip_pad(s1, s2, pad='null'))

print('''
using generators: yield
def myzip(*seqs):
    seqs = [list(s) for s in seqs]
    while all(seqs):
        yield tuple(s.pop(0) for s in seqs)
''')
def myzip(*seqs):
    seqs = [list(s) for s in seqs]
    while all(seqs):
        yield tuple(s.pop(0) for s in seqs)

print('list(myzip(s1, s2)) =', list(myzip(s1, s2)))

print('''
def myzip_pad(*seqs, pad=None):
    seqs = [list(s) for s in seqs]
    while any(seqs):
        yield tuple((s.pop(0) if s else pad) for s in seqs)
''')
def myzip_pad(*seqs, pad=None):
    seqs = [list(s) for s in seqs]
    while any(seqs):
        yield tuple((s.pop(0) if s else pad) for s in seqs)

print('list(myzip_pad(s1, s2)) =', list(myzip_pad(s1, s2)))
print("list(myzip_pad(s1, s2, pad='null')) =", list(myzip_pad(s1, s2, pad='null')))

print('''
alternate implementation with lengths
def myzip(*seqs):
    minlen = min(len(s) for s in seqs)
    return [tuple(s[i] for s in seqs) for i in range(minlen)]
''')

def myzip(*seqs):
    minlen = min(len(s) for s in seqs)
    return [tuple(s[i] for s in seqs) for i in range(minlen)]

print('myzip(s1, s2) =', myzip(s1, s2))

print('''
def myzip_pad(*seqs, pad=None):
    maxlen = max(len(s) for s in seqs)
    index = range(maxlen)
    return [tuple((s[i] if len(s) > i else pad) for s in seqs) for i in index]
''')
def myzip_pad(*seqs, pad=None):
    maxlen = max(len(s) for s in seqs)
    index = range(maxlen)
    return [tuple((s[i] if len(s) > i else pad) for s in seqs) for i in index]

print('myzip_pad(s1, s2) =', myzip_pad(s1, s2))
print("myzip_pad(s1, s2, pad='null') =", myzip_pad(s1, s2, pad='null'))

print('''
using generators: (...)
def myzip(*seqs):
    minlen = min(len(s) for s in seqs)
    return (tuple(s[i] for s in seqs) for i in range(minlen))
''')
def myzip(*seqs):
    minlen = min(len(s) for s in seqs)
    return (tuple(s[i] for s in seqs) for i in range(minlen))

print('list(myzip(s1, s2)) =', list(myzip(s1, s2)))
