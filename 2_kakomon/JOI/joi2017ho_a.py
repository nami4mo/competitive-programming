import sys
input = sys.stdin.readline
n,q,s,t=map(int, input().split())
al=[int(input()) for _ in range(n+1)]
dl=[a2-a1 for a2,a1 in zip(al[1:],al[:-1])]
# print(dl)

ans=0
for d in dl:
    if d>0: ans-=d*s
    else: ans-=d*t
# -max(0,d)*s-min(0,d)*t

ansl=[]
for _ in range(q):
    l,r,x=map(int, input().split())
    l-=1
    prev_lv=-max(0,dl[l])*s-min(0,dl[l])*t
    dl[l]+=x
    lv=-max(0,dl[l])*s-min(0,dl[l])*t
    ans+=(lv-prev_lv)

    if r<n:
        prev_rv=-max(0,dl[r])*s-min(0,dl[r])*t
        dl[r]-=x
        rv=-max(0,dl[r])*s-min(0,dl[r])*t
        ans+=(rv-prev_rv)
    ansl.append(ans)

for a in ansl:print(a)