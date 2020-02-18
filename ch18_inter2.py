def intersect(*args):
    res = []
    for x in args[0]:
        for other in args[1:]:
            if not x in other: break
        else:
            res.append(x)
    return res

def union(*args):
    res = []
    for seq in args:
        for x in seq:
            if not x in res:
                res.append(x)
    return res

s1 = 'SPAM'
s2 = 'SCAM'
s3 = 'SCBM'
print('s1 = %s, s2 = %s, s3 = %s' % (s1, s2, s3))

print('intersect(s1, s2) =', intersect(s1, s2))
print('union(s1, s2) =', union(s1, s2))
print('intersect([1, 2, 3], (1, 4)) =', intersect([1, 2, 3], (1, 4)))
print('intersect(s1, s2, s3) =', intersect(s1, s2, s3))
print('union(s1, s2, s3) =', union(s1, s2, s3))
