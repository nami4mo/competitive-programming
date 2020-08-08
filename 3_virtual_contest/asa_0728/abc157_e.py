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


def main():
    n = int(input())
    s = list(input())
    q = int(input())
    alps = 'abcdefghijklmnopqrstuvwxyz'

    
    alp_d = {chr(ord('a') + i): Bit(n) for i in range(26)}
    for i,si in enumerate(s):
        alp_d[si].add(i+1,1) 

    ansl = []
    for i in range(q):
        com,a,b = map(str, input().split())
        if com == '1':
            i,c = int(a),b
            si = s[i-1]
            alp_d[si].add(i, -1)
            alp_d[c].add(i, 1)
            s[i-1] = c
        else:
            l,r = int(a),int(b)
            ans = 0
            for alp in alps:
                cnt = alp_d[alp].sum(r) - alp_d[alp].sum(l-1)
                if cnt > 0:
                    ans+=1
            ansl.append(ans)

    for a in ansl:
        print(a)


if __name__ == "__main__":
    main()