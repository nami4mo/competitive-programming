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

    def lower_bound(self, x):
        """ 累積和がx以上になる最小のindexと、その直前までの累積和 """
        sum_ = 0
        pos = 0
        for i in range(self.depth, -1, -1):
            k = pos + (1 << i)
            if k <= self.size and sum_ + self.tree[k] < x:
                sum_ += self.tree[k]
                pos += 1 << i
        return pos, sum_

    def get_less_than_x_cnt(self, x):
        """ 累積和がx未満 の個数 """
        lb_pos, lb_sum = self.lower_bound(x)
        return lb_pos-1

    def get_less_than_and_x_cnt(self, x):
        """ 累積和がx以下 の個数 """
        lb_pos, lb_sum = self.lower_bound(x+1)
        return lb_pos-1
    
    def get_more_than_x_cnt(self, x):
        """ 累積和がxより大きい 個数 """
        return self.size - self.get_less_than_and_x_cnt(x)


n=int(input())
al=list(map(int, input().split()))
bl=list(map(int, input().split()))
al=[a+i for i,a in enumerate(al)]
bl=[b+i for i,b in enumerate(bl)]

ds={}
num=0
bbl=[]
for b in bl:
    if b in ds:
        bbl.append(ds[b])
    else:
        ds[b]=num
        num+=1
        bbl.append(ds[b])

from collections import deque
aal=[deque() for _ in range(num)]
for i,a in enumerate(al):
    if a not in ds:
        print(-1)
        exit()
    aal[ds[a]].append(i)

bit=Bit(n)
ans=0
# print(aal)
for i,b in enumerate(bbl):
    if not aal[b]:
        print(-1)
        exit()
    ind=aal[b].popleft()
    orig_ind=ind
    # print(i,ind)
    ind+=bit.sum(0,ind+1)
    # print(i,ind)
    # print('---')
    ans+=abs(ind-i)
    bit.add(0,1)
    bit.add(orig_ind,-1)
print(ans)