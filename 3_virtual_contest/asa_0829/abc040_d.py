from collections import deque

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    # too slow
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def get_all_members(self):
        pare_d = {}
        for i in range(self.n):
            parent = self.find(i)
            pare_d.setdefault(parent,[])
            pare_d[parent].append(i)
        return list(pare_d.values())

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())



n,m = map(int, input().split())
yabl = []
for _ in range(m):
    a,b,y = map(int, input().split())
    yabl.append((y,a,b))

yabl.sort(reverse=True)
qy = deque(yabl)

wvil = []
q = int(input())
for i in range(q):
    v,w = map(int, input().split())
    wvil.append((w,v,i))

wvil.sort(reverse=True)
qq = deque(wvil)

uf = UnionFind(n+1)
prev = qy[0][0]
first = True
ansl = [0]*q

while qq and qq[0][0] >= prev:
    w,v,i = qq.popleft()
    ansl[i] = 1

while qy:
    while qy and (prev == qy[0][0] or first):
        y,a,b = qy.popleft()
        # print(y,a,b)
        uf.union(a,b)
        prev = y
        first = False

    nexty = qy[0][0] if qy else -1
    while qq and qq[0][0] >= nexty:
        w,v,i = qq.popleft()
        # print('---',w,v,i)
        cnt = uf.size(v)
        ansl[i] = cnt

    first = True

    
for a in ansl: print(a)