n=int(input())
vl=[]
for _ in range(n):
    row=list(map(int, input().split()))
    vl.append(row)

from itertools import product
from typing import ByteString
ite = list(product(range(3),repeat=5))
# for pattern in ite:
#     for i, v in enumerate(pattern):
#         pass

# print(ite)

ok, ng = 0, 10**9+10
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    res = False
    dp=[[False]*32 for _ in range(4)]
    dp[0][0]=True
    for row in vl:
        val=0
        for i,v in enumerate(row):
            if v>=mid:val+=(1<<i)
        for i in range(3):
            for bit in range(1<<5):
                if dp[i][bit]: dp[i+1][bit|val]=True
    if dp[3][31]:
        res=True
    else:
        res=False

    # for pattern in ite:
    #     needs=[[] for _ in range(3)]
    #     for i,v in enumerate(pattern):
    #         needs[v].append(i)

    #     oks=[False]*3
    #     for row in vl:
    #         for i in range(3):
    #             ok=True
    #             for need in needs[i]:
    #                 if row[need]<mid:
    #                     ok=False
    #                     break
    #             if ok: oks[i]=True
    #     if oks[0] and oks[1] and oks[2]:
    #         res=True
    #         break
    #     else:
    #         res=False
    
    if res: ok = mid
    else: ng = mid
print(ok)