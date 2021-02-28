ansl=[]
for _ in range(int(input())):
    n,k=map(int, input().split())
    al=list(map(int, input().split()))
    ans=0
    curr=al[0]
    for a in al[1:]:
        dmin=(100*a-k*curr-1)//k +1
        ans=max(dmin,ans)
        curr+=a
    ansl.append(ans)
for a in ansl:print(a)