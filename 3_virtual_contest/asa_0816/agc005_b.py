''' 
    [Bit]
'''
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
bit = Bit(n)

a_to_i = [0]*(n+1)
for i,a in enumerate(al):
    a_to_i[a] = i+1

ans = 0
for a in range(1,n+1):
    curr_i = a_to_i[a]
    all_left_cnt = bit.sum(curr_i)
    if all_left_cnt == 0:
        left_cnt = curr_i
        left_i = 0
    else:
        left_i, _ = bit.lower_bound(all_left_cnt)
        left_cnt = curr_i - left_i

    right_i, _ = bit.lower_bound(all_left_cnt+1)
    right_cnt = right_i - curr_i
    all_cnt = right_cnt*left_cnt
    a_sum = a*all_cnt
    ans += a_sum
    bit.add(curr_i,1)

print(ans)