from collections import deque
from bisect import bisect_left, bisect_right
from itertools import accumulate


n,m,k = map(int, input().split())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))

al_sums = list(accumulate(al))
bl_sums = list(accumulate(bl))

ans = 0
for i in range(0,n+1):
    if i == 0: 
        a_sum = 0
    else:
        a_sum = al_sums[i-1]
    if a_sum > k: 
        continue
    cnt = bisect_right(bl_sums, k-a_sum)
    curr_ans = i+cnt
    ans = max(ans,curr_ans)

print(ans)