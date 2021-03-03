
# https://atcoder.jp/contests/abc140/tasks/abc140_e
# https://atcoder.jp/contests/agc005/tasks/agc005_b
# https://atcoder.jp/contests/abc157/tasks/abc157_e

''' 
    [Bit]
'''
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


n,q=map(int, input().split())
qs=[]
for i in range(n-1):
    l,r=map(int, input().split())
    qs.append((l,'open',i))
    qs.append((r+1,'close',i))


abl=[(-1,-1)]*q
for i in range(q):
    a,b=map(int, input().split())
    qs.append((a,b,'q',i))

qs.sort(key=lambda x:x[0])

# 0:open, 1:close
bit=Bit(n)
for i in range(1,n):
    bit.add(i,1)

# print(qs)
ansl=[-1]*q
for query in qs:
    if query[1]=='open':
        bit.add(query[2]+1,-1)
    elif query[1]=='close':
        bit.add(query[2]+1,1)
    else:
        b,i=query[1],query[3]
        b-=1
        v=bit.sum(0,b+1)
        left,_=bit.lower_bound(v)
        right,_=bit.lower_bound(v+1)
        dist=right-left
        ansl[i]=dist
        # print('---',i,left,right,v)
        # for i in range(1,n): print(bit.sum(i,i+1),end=' ')
        # print()
for a in ansl:print(a)