print('class c_set, def intersect/union/concat')
class c_set:
    def __init__(self, value = []):
        self.data = []
        self.concat(value)
    def intersect(self, other):
        res = []
        for x in self.data:
            if x in other:
                res.append(x)
        return c_set(res)
    def union(self, other):
        res = self.data[:]
        for x in other:
            if not x in res:
                res.append(x)
        return c_set(res)
    def concat(self, value):
        for x in value:
            if not x in self.data:
                self.data.append(x)
    def __len__(self): return len(self.data)
    def __getitem__(self, key): return self.data[key]
    def __and__(self, other): return self.intersect(other)
    def __or__(self, other): return self.union(other)
    def __repr__(self): return 'c_set: ' + repr(self.data)

if __name__ == '__main__':
    print()
    print('self test')
    print('x = c_set([1, 3, 5, 7])')
    x = c_set([1, 3, 5, 7])
    print('y = c_set([1, 4, 7])')
    y = c_set([1, 4, 7])
    print('z = c_set([1, 4, 6])')
    z = c_set([1, 4, 6])
    print('x.union(y) =', x.union(y))
    print('x | z =', x | z)
