
# https://atcoder.jp/contests/abc140/tasks/abc140_e
# https://atcoder.jp/contests/agc005/tasks/agc005_b
# https://atcoder.jp/contests/abc157/tasks/abc157_e

''' 
    [Bit]
'''
def modinv(a,m):
    b, u, v = m, 1, 0
    while b:
        t = a//b
        a -= t*b
        a,b = b,a
        u -= t * v
        u,v = v,u
    u %= m
    return u
    

MOD=998244353
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
            if s>MOD:s-=MOD
            i -= i & -i
        return s

    def sum(self,l,r):
        return (self._sum(r-1)-self._sum(l-1))%MOD
 
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


# if __name__ == "__main__":
#     bit=Bit(5)
#     bit.add(0,1)
#     bit.add(1,2)
#     bit.add(2,3)
#     bit.add(3,4)
#     bit.add(4,5)
#     print(bit.lower_bound(2))

def main():
    n=int(input())
    al=list(map(int, input().split()))
    ail=[(a,i) for i,a in enumerate(al)]
    ail.sort()
    bit=Bit(n+1)
    p2=[1]
    for i in range(n):
        p2.append((p2[-1]*2)%MOD)
    ans=0
    for a,i in ail:
        bit.add(i, p2[n-1-i])
        val=bit.sum(0,i)
        dist=n-i
        val*=modinv(p2[dist],MOD)
        ans+=val
        ans%=MOD
    print(ans)


if __name__ == "__main__":
    main()