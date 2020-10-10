
# # https://atcoder.jp/contests/abc140/tasks/abc140_e
# # https://atcoder.jp/contests/agc005/tasks/agc005_b
# # https://atcoder.jp/contests/abc157/tasks/abc157_e

# ''' 
#     [Bit]
# '''
# class Bit:
#     """ used for only int(>=0) 
#         1-indexed (ignore 0-index)
#     """
#     def __init__(self, n):
#         self.size = n
#         self.tree = [0] * (n + 1)
#         self.depth = n.bit_length()
 
#     def sum(self, i):
#         s = 0
#         while i > 0:
#             s += self.tree[i]
#             i -= i & -i
#         return s
 
#     def add(self, i, x):
#         while i <= self.size:
#             self.tree[i] += x
#             i += i & -i

#     def lower_bound(self, x):
#         """ 累積和がx以上になる最小のindexと、その直前までの累積和 """
#         sum_ = 0
#         pos = 0
#         for i in range(self.depth, -1, -1):
#             k = pos + (1 << i)
#             if k <= self.size and sum_ + self.tree[k] < x:
#                 sum_ += self.tree[k]
#                 pos += 1 << i
#         return pos + 1, sum_

#     def get_less_than_x_cnt(self, x):
#         """ 累積和がx未満 の個数 """
#         lb_pos, lb_sum = self.lower_bound(x)
#         return lb_pos-1

#     def get_less_than_and_x_cnt(self, x):
#         """ 累積和がx以下 の個数 """
#         lb_pos, lb_sum = self.lower_bound(x+1)
#         return lb_pos-1
    
#     def get_more_than_x_cnt(self, x):
#         """ 累積和がxより大きい 個数 """
#         return self.size - self.get_less_than_and_x_cnt(x)

# MAX = 200001
# # MAX = 5
# bit = Bit(MAX)
# for i in range(1,MAX+1):
#     bit.add(i,1)

# already = [False]*MAX
# n = int(input())
# pl = list(map(int, input().split()))
# ansl = []
# for p in pl:
#     if not already[p]:
#         bit.add(p,-1)
#         already[p] = True
#     # print(bit.tree)
#     ans,_ = bit.lower_bound(1)
#     # print(ans)
#     ansl.append(ans)

# for a in ansl: print(a)

MAX = 200001
n = int(input())
pl = list(map(int, input().split()))
curr_pos = 0
already = [False]*MAX

for p in pl:
    if p == curr_pos:
        while True:
            curr_pos += 1
            if already[curr_pos] == False:
                break
    print(curr_pos)
    already[p] = True
