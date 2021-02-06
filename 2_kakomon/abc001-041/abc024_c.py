n,d,k=map(int, input().split())
dl=[tuple(map(int, input().split())) for _ in range(d)]
stl=[tuple(map(int, input().split())) for _ in range(k)]

for s,t in stl:
    curr=s
    posi=1 if s<t else -1
    for i in range(d):
        l,r=dl[i]
        if posi==1 and l<=curr<=r:
            curr=r
            if curr>=t:
                print(i+1)
                break
        elif posi==-1 and l<=curr<=r:
            curr=l
            if curr<=t:
                print(i+1)
                break