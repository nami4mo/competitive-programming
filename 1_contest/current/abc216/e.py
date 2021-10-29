n,k=map(int, input().split())
al=list(map(int, input().split()))
al.sort(reverse=True)

al.append(-1)

ans=0
ind=0
while k>0 and ind<n:
    d=al[ind]-al[ind+1]
    cnt=ind+1
    max_play=d*cnt
    if k>=max_play:
        a=al[ind+1]
        val=cnt*d*(2*a+d+1)//2
        ans+=val
        k-=max_play
    else:
        okcnt=k//cnt
        a=al[ind]-okcnt+1
        val=cnt*okcnt*(a+al[ind])//2
        ans+=val
        rem=k%cnt
        ans+=rem*(a-1)
        k=0
    ind+=1
print(ans)