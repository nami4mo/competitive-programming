
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

BIT_OFFSET=10**5+1
def check(x,n,al):
    bit=Bit(3*10**5)
    cnt=0
    csum=0
    bit.add(0+BIT_OFFSET,1)
    for a in al:
        v = 1 if a>=x else -1
        csum+=v
        cnt+=bit.sum(0,csum+BIT_OFFSET+1)
        bit.add(csum+BIT_OFFSET,1)
    comb=n*(n+1)//2
    half=(comb+1)//2
    if cnt>=half:return True
    else: return False


n=int(input())
al=list(map(int, input().split()))

ok, ng = 0, 10**9+1
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    ok_flag = check(mid,n,al)
    # ...
    if ok_flag:
        ok = mid
    else:
    	ng = mid
print(ok)