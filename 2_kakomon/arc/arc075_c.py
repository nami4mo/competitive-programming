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


n,k=map(int, input().split())
al=[int(input())-k for _ in range(n)]
cl=[]
c=0
for i,a in enumerate(al):
    c+=a
    cl.append((c,i))

cl.sort()
# print(cl)
bit=Bit(n)
ans=0
for c,i in cl:
    ans+=(bit.sum(0,i))
    if c>=0:ans+=1
    bit.add(i,1)
print(ans)