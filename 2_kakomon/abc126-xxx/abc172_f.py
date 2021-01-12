from functools import lru_cache
import sys
sys.setrecursionlimit(10**6)
#  min x such as (a0-x)^(a1+x) = goal
INF=10**20
@lru_cache(None)
def rec(a0,a1,goal,keta):
    if a0==0:
        return INF
    if a0^a1==goal:
        return 0
    if (a0^a1)%2 != goal%2:
        return INF
    if goal==0:
        if a0<a1 or (a0+a1)%2==1: return INF
        return pow(2,keta)*(a0-a1)//2
    res=INF
    res=min(res, rec((a0-1)//2, (a1+1)//2, goal//2, keta+1)+pow(2,keta))
    res=min(res, rec(a0//2, a1//2, goal//2, keta+1))
    return res

n=int(input())
al=list(map(int, input().split()))
a0=al[0]
a1=al[1]
goal=0
for a in al[2:]:
    goal=goal^a

ans=rec(a0,a1,goal,0)
if ans>=INF:ans=-1
print(ans)