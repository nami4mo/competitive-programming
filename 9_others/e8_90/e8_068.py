
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


n=int(input())
q=int(input())
bit=Bit(n+1)
bit2=Bit(n+1)
used=[False]*(n+1)
INF=10**18
for i in range(n+1):
    bit.add(i,INF)
    bit2.add(i,INF)

al=[]
for _ in range(q):
    t,x,y,v=map(int, input().split())
    x-=1
    y-=1
    if t==0:
        if used[x]:continue
        used[x]=True
        if x%2==0:
            bit.add(x,-INF+v)
            bit2.add(x,-INF)
        else:
            bit.add(x,-INF-v)
            bit2.add(x,-INF)
    else:
        if x==y:
            al.append(v)
            continue
        sumval=bit.sum(min(x,y),max(x,y))
        # print('--',sumval)
        if x<y:
            if y%2==0:sumval*=(-1)
        else:
            if y%2==1:sumval*=(-1)
        if (y-x)%2==1:v*=(-1)
        ans=sumval+v
        # if ans>=10**14+10:
        #     ans='Ambiguous'
        if bit2.sum(min(x,y),max(x,y))>=INF:
            ans='Ambiguous'
        al.append(ans)
        # print(ans)
for a in al:print(a)
    