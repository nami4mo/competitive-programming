
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


def main():
    n = int(input())
    s = list(input())
    q = int(input())
    ql = []
    for _ in range(q): 
        num,a,b = map(str, input().split())
        ql.append((num,a,b))
    alp_d = {chr(ord('a') + i): Bit(n) for i in range(26)}

    for i, si in enumerate(s):
        alp_d[si].add(i+1,1)

    for query in ql:
        a,b,c = query
        if a == '1':
            b = int(b)
            before = s[b-1]
            alp_d[before].add(b, -1)
            alp_d[c].add(b,1)
            s[b-1] = c
        else:
            l,r = int(b),int(c)
            cnt = 0
            for v in alp_d.values():
                if v.sum(r)-v.sum(l-1) > 0:
                    cnt += 1
            print(cnt) 


if __name__ == "__main__":
    main()