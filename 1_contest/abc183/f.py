from collections import deque
from copy import copy
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

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



n,q = map(int, input().split())
cl = [-1] + list(map(int, input().split()))
uf = UnionFind(n+1)
uf_cnts = [{} for _ in range(n+1)]
for i in range(n+1):
    uf_cnts[i][cl[i]] = 1

qq = [ deque() for _ in range(n+1)]
for _ in range(q):
    q,a,b = map(int, input().split())
    # print(qq)
    if q == 1:
        if not uf.same(a,b):
            if uf.size(a) < uf.size(b):
                a,b = b,a
            old_p = uf.find(b)
            uf.union(a,b)
            new_p = uf.find(a)
            # print('np',new_p)
            for k,v in uf_cnts[old_p].items():
                if not k in uf_cnts[new_p]:
                    uf_cnts[new_p][k] = 0
                uf_cnts[new_p][k] += v   
            # print(uf_cnts)
    else:
        pare_a = uf.find(a)
        if b in uf_cnts[pare_a]:
            print(uf_cnts[pare_a][b])
        else:
            print(0)