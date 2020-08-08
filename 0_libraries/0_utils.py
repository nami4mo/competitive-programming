

# ------------ input ------------ 
import sys
input = sys.stdin.readline
input().rstrip() # remove last '\n'

n = int(input())
s = input()
sl = list(input()) # abc -> ['a', 'b', 'c']
a, b = map(int, input().split()) 
al = list(map(int, input().split())) 


# ------------ str manipulation ------------
import string 
alp = string.ascii_lowercase
alp = 'abcdefghijklmnopqrstuvwxyz'
alp = [chr(ord('a')+i) for i in range(26)]
alp_d = {chr(ord('a') + i): 0 for i in range(26)}

ALP = string.ascii_uppercase
ALP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ALP = alp.upper()
alp = ALP.lower()

alps = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


# --- bisect
a,b,x = map(int, input().split())

ok, ng = 0,10**9+1
while abs(ok-ng) > 1:
    mid = (ok+ng) // 2
    price = a*mid + b*len(str(mid))
    if price <= x:
        ok = mid
    else:
    	ng = mid
print(ok)

# ------------ list ------------
## list * -1
al = [a*(-1) for a in al]

# 3-dim
# dp[N][M][L]
dp = [ [ [0]*L  for _ in range(M) ] for _ in range(N) ]


# binary search
from bisect import bisect_left, bisect_right
a_list = [1,3,3,3,6,6,7,10]
bisect_left(a_list,4) # -> 4
bisect_right(a_list,4) # -> 4
bisect_left(a_list,3) # -> 1
bisect_right(a_list,3) # -> 4


# 2分探索
left = 0
right = 2*(10**16)
while True:
    mid = left + (right-left)//2
    res = True
    if res: right = mid
    else:   left = mid
    if right - left <= 1:
        break


# ---- negetive/zero/positive counts
al = list(map(int, input().split()))
al.sort()
n_cnt = bisect_right(al,-1)
p_cnt = n - bisect_left(al,1)
zero_cnt = n-p_cnt-n_cnt
print(n_cnt, p_cnt, zero_cnt)


# ------- HeapDict ----------
import heapq
class HeapDict:
    def __init__(self):
        self.h = []
        self.d = {}

    def insert(self,x):
        if x not in self.d or self.d[x] == 0:
            heapq.heappush(self.h, x)
        self.d.setdefault(x,0)
        self.d[x] += 1


    def erase(self,x):
        if x not in self.d or self.d[x] == 0:
            return
        else:
            self.d[x] -= 1

        while self.h:
            if self.d[self.h[0]] == 0:
                heapq.heappop(self.h)
            else:
                break


    def get_min(self):
        if not self.h:
            return None
        else:
            return self.h[0]


    def pop(self):
        poped_val = self.h[0]
        self.erase(poped_val)
        return poped_val


    def exist(self, x):
        return (x in self.d and self.d[x] > 0)


    def show_h(self):
        elems = [v for v in self.h if self.d[v] > 0]
        print(elems)


    def show_d(self):
        print(self.d)


# ----- BIT -----
class Bit:
    """ used for only int(>=0) 
        1-indexed (ignore 0-index)
    """
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
        self.depth = n.bit_length()
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
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
        return pos + 1, sum_

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
