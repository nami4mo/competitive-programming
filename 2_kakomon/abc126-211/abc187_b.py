class Bit:
    """ 
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


n=int(input())
xyl_m45=[]
for _ in range(n):
    x,y=map(int, input().split())
    xyl_m45.append((x+y,-x+y+3*10**3))

MAX_Y=10**4
bit=Bit(MAX_Y)
xyl_m45.sort(key=lambda x: (-x[0],x[1]))
ans=0
for x,y in xyl_m45:
    ans+=bit.sum(0,y+1)
    bit.add(y,1)

print(ans)