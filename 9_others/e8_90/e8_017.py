class Bit:
    """ used for only int(>=0) 
        0-indexed 
    """
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
        self.depth = n.bit_length()
 
    def _sum(self, i):
        i+=1
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def sum(self,l,r):
        return self._sum(r-1)-self._sum(l-1)
 
    def add(self, i, x):
        i+=1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i



n,m=map(int, input().split())
lrs=[]
for _ in range(m):
    l,r=map(int, input().split())
    if l>r:l,r=r,l
    lrs.append((l,r))

lrs.sort(key=lambda x:(x[0],-x[1]))
ans=0

bit=Bit(n+1)
for l,r in lrs:
    bit.add(r,1)
    cnt=bit.sum(l+1,r)
    ans+=cnt
print(ans)
