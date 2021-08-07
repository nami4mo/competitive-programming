n=int(input())
al=list(map(int, input().split()))
bl=list(map(int, input().split()))
amax=0
cmax=0
for i in range(n):
    ai=al[i]
    bi=bl[i]
    if ai>amax:
        cand1=ai*bi
        cand2=amax*bi
        cand3=cmax
        ans=max(cand1,cand2,cand3)
        print(ans)
        cmax=ans
        amax=ai
    else:
        cand2=amax*bi
        cand3=cmax
        ans=max(cand2,cand3)
        cmax=ans
        print(ans)
