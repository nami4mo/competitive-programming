import sys
input = sys.stdin.readline
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


n = int(input())
al = list(map(int, input().split()))

bit23 = Bit(10**5)
bit45 = Bit(10**5)
bit67 = Bit(10**5)
bit8 = Bit(10**5)

cnts = [0]*(10**5+1)
for a in al:
    cnts[a] += 1
    if cnts[a] == 2: 
        bit23.add(a,1)
    elif cnts[a] == 4: 
        bit45.add(a,1)
        bit23.add(a,-1)
    elif cnts[a] == 6: 
        bit67.add(a,1)
        bit45.add(a,-1)
    elif cnts[a] == 8: 
        bit8.add(a,1)
        bit67.add(a,-1)

for _ in range(int(input())):
    sig,a = map(str, input().split())
    a = int(a)
    if sig == '+':
        cnts[a] += 1
        if cnts[a] == 2: 
            bit23.add(a,1)
        elif cnts[a] == 4: 
            bit45.add(a,1)
            bit23.add(a,-1)
        elif cnts[a] == 6: 
            bit67.add(a,1)
            bit45.add(a,-1)
        elif cnts[a] == 8: 
            bit8.add(a,1)
            bit67.add(a,-1)
    else:
        cnts[a] -= 1
        if cnts[a] == 1: 
            bit23.add(a,-1)
        elif cnts[a] == 3: 
            bit45.add(a,-1)
            bit23.add(a,1)
        elif cnts[a] == 5: 
            bit67.add(a,-1)
            bit45.add(a,1)
        elif cnts[a] == 7: 
            bit8.add(a,-1)
            bit67.add(a,1)

    cnt8 = bit8.sum(10**5)
    cnt6 = bit67.sum(10**5)
    cnt4 = bit45.sum(10**5)
    cnt2 = bit23.sum(10**5)

    if cnt8 >= 1: print('YES')
    elif cnt6 >= 2: print('YES')
    elif cnt6 == 1 and cnt2+cnt4 >= 1: print('YES')
    elif cnt4 >= 2: print('YES')
    elif cnt4 == 1 and cnt2 >= 2: print('YES')
    else: print('NO')