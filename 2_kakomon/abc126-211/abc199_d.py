import sys
sys.setrecursionlimit(10**6)

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

p3=[]
for i in range(21):
    p3.append(pow(3,i))

ans=[0]
def dfs(cs,node,nodes,cnt,gl,n,ans,used):
    if cnt==n:
        check=True
        # print(cs)
        val=0
        for i,c in enumerate(cs):
            val+=p3[i]*c
        if val in used:return
        used.add(val)

        for cn in nodes:
            for neib in gl[cn]:
                if cs[cn]==cs[neib]:
                    check=False
                    break
            if not check:break
        if check: ans[0]+=1
        return 

    for neib in gl[node]:
        if cs[neib]!=-1:continue
        for c in [0,1,2]:
            if c==cs[node]:continue
            cs[neib]=c
            dfs(cs, neib, nodes, cnt+1, gl,n, ans,used)
            cs[neib]=-1


def solve(nodes,gl):
    n=len(nodes)
    cs=[-1]*n
    # s=nodes[0]
    ans=[0]
    cs[0]=0
    used=set()
    dfs(cs,0,nodes,1,gl,n,ans,used)
    return ans[0]*3

n,m=map(int, input().split())
uf=UnionFind(n)
gl=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int, input().split())
    a-=1
    b-=1
    gl[a].append(b)
    gl[b].append(a)
    uf.union(a,b)

nodes=uf.get_all_members()
# print(nodes)
pat=1
for gr in nodes:
    pat*=solve(gr,gl)

print(pat)