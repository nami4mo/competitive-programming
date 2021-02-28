ansl=[]
for _ in range(int(input())):
    n=int(input())
    cl=list(map(int, input().split()))
    al=list(map(int, input().split()))
    bl=list(map(int, input().split()))
    reset=True
    ans=0
    cnt=0
    for i in range(n-1,0,-1):
        if reset:
            cnt=cl[i]-1+2
        else:
            a,b=al[i+1],bl[i+1]
            if a>b:a,b=b,a
            dist=max(cnt+a-1+cl[i]-b,cl[i]-1)
            cnt=dist+2
        end_dist=abs(al[i]-bl[i])
        ans=max(ans,cnt+end_dist)
        if al[i]==bl[i]:
            cnt=0
            reset=True
        else:
            reset=False
    ansl.append(ans)

for a in ansl:print(a)