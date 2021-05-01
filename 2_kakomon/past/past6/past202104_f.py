n,l,t,x=map(int, input().split())
abl=[]
for _ in range(n):
    a,b=map(int, input().split())
    abl.append((a,b))

ans=0
fuka=0
for i in range(n):
    if b>=l and a>t:
        print('forever')
        exit()

    a,b=abl[i]
    if b<l:
        fuka=0
        ans+=a
    else:
        if fuka+a>t:
            ans+=(t-fuka)
            ans+=x
            ans+=a
            fuka=a
        else:
            ans+=a
            fuka+=a

    if fuka==t:
        ans+=x
        fuka=0

    # print(ans,fuka)
print(ans)