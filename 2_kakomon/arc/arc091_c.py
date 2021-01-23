'''
    experiment
'''
# from itertools import permutations
# from bisect import bisect_left
# def lis(al):
#     n=len(al)
#     INF=10**10
#     dp = [INF]*(n+1)
#     dp[0] = -INF
#     for i, a in enumerate(al):
#         ind = bisect_left(dp, a) # max index of "value <= a"
#         dp[ind] = a
#     ans = bisect_left(dp, INF) - 1 # cnt of "value < INF" and remove 0-index
#     return ans

# n, k = 10, 10
# ll = list(range(1,n+1))  # list of elements
# perml = list(permutations(ll, k))
# ds={}
# for perm in perml:
#     permr=[10-v for v in perm]
#     print(perm, lis(perm), lis(permr))
#     ans=(lis(perm),lis(permr))
#     ds.setdefault(ans,0)
#     ds[ans]+=1

# print(ds)

from collections import deque
n,a,b=map(int, input().split())
if a*b<n or a+b>n+1:
    print(-1)
    exit()

top=0
for i in range(n+1):
    loop=(n-i)//b
    just=0
    if (n-i)%b!=0: just=1
    up=i+loop+just
    if up==a:
        top=i
        break

q=deque()
full_loop=(n-top)//b
for i in range(full_loop):
    start=(i+1)*b
    for j in range(b):
        val=start-j
        q.append(val)

if a*b==n:
    ansl=list(q)
    print(*ansl)
    exit()

curr_lis=full_loop+1
for i in range((n-top)%b):
    val=(n-top)-i
    q.append(val) 

for i in range(top):
    q.appendleft(i*(-1))

ansl=list(q)
ansl=[a+top for a in ansl]
print(*ansl)
