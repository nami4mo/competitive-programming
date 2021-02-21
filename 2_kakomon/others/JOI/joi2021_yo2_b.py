# def flip(v,m,n):
#     cv=v
#     res=0
#     for i in range(n):
#         if i<=m:
#             res+=pow(3,m-i)*(cv%3)
#         else:
#             res+=pow(3,i)*(cv%3)
#         cv//=3            
#     return res

from collections import deque

n,q=map(int, input().split())
dp=[-1]*(3**n)
que=deque()
for i in range(n+1):
    for j in range(n+1):
        k=n-i-j
        if k<0:continue
        v3=0
        for keta in range(n):
            if keta<i: v3+=0
            elif i<=keta<i+j: v3+=pow(3,keta)*1
            else: v3+=pow(3,keta)*2
        dp[v3]=0
        que.append(v3)

loop=0
while que:
    loop+=1
    poped=que.popleft()
    right=poped
    left=0
    cv=poped
    for i in range(n):
        v3=cv%3
        right-=pow(3,i)*v3
        left*=3
        left+=v3
        flipped=right+left
        # flipped=flip(poped,i,n)
        cv//=3
        if dp[flipped]!=-1:continue
        dp[flipped]=dp[poped]+1
        que.append(flipped)
# print(loop)

ansl=[]
for _ in range(q):
    s=input()
    v=0
    for i in range(n):
        if s[i]=='A': v+=0
        if s[i]=='B': v+=pow(3,i)*1
        if s[i]=='C': v+=pow(3,i)*2
    ans=dp[v]
    ansl.append(ans)
for a in ansl:print(a)