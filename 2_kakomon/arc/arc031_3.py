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

# def solve(n,al):
#     # n=int(input())
#     # al=list(map(int, input().split()))

#     left_tentos=[0]
#     tento=0
#     bit=Bit(n+1)
#     for i in range(n):
#         a=al[i]
#         tento+=(i-bit.sum(0,a))
#         left_tentos.append(tento)
#         bit.add(a,1)

#     right_tentos=[0]
#     tento=0
#     bit=Bit(n+1)
#     alr=al[::-1]
#     for i in range(n):
#         a=alr[i]
#         tento+=(i-bit.sum(0,a))
#         right_tentos.append(tento)
#         bit.add(a,1)

#     # print(left_tentos)
#     # print(right_tentos)

#     ans=10**16
#     for lcnt in range(0,n+1):
#         rcnt=n-lcnt
#         v=left_tentos[lcnt]+right_tentos[rcnt]
#         ans=min(ans,v)
#     return ans


# def solve2(n,al):

n=int(input())
al=list(map(int, input().split()))
ail=[(a,i) for i,a in enumerate(al)]
ail.sort()

lc=0
rc=0
ans=0

# print(ail)
bit=Bit(n+1)
for a,i in ail:
    ld=i-bit.sum(0,i)
    rd=n-1-i-bit.sum(i,n+1)
    bit.add(i,1)
    ans+=min(ld,rd)
print(ans)