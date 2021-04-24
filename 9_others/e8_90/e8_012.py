

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        ## if parents[i]>=0 => parents[i] is parent of i
        ## if parents[i]<0 => i is root and (-1)*parents[i] shows the group size.

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

        # if size[x] < size[y]: => swap (x group: larger, y group: smaller)
        # to merge the smaller group(y) into the larger(x)
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



h,w=map(int, input().split())
uf=UnionFind(h*w)
cl=[[False]*w for _ in range(h)]

def pv(y,x):return y*w+x

for _ in range(int(input())):
    ql=list(map(int, input().split()))
    if ql[0]==1:
        r,c=ql[1]-1,ql[2]-1
        cl[r][c]=True
        for dy,dx in [(-1,0),(1,0),(0,1),(0,-1)]:
            yy=r+dy
            xx=c+dx
            if not (0<=yy<h and 0<=xx<w):continue
            if cl[yy][xx]:uf.union(pv(r,c),pv(yy,xx))
    else:
        r1,c1,r2,c2=ql[1]-1,ql[2]-1,ql[3]-1,ql[4]-1
        if uf.same(pv(r1,c1),pv(r2,c2)) and cl[r1][c1]:
            print('Yes')
        else:
            print('No')