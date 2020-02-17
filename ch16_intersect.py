def intersect(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res

s1 = 'SPAM'
s2 = 'SCAM'
print('s1 =', s1)
print('s2 =', s2)
print('intersect(s1, s2) =', intersect(s1, s2))

print('intersect([1, 2, 3], (1, 4)) =', intersect([1, 2, 3], (1, 4)))
