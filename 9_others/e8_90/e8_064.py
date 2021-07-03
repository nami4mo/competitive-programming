n,q=map(int, input().split())
al=list(map(int, input().split()))
dl=[]
csum=0
for i in range(n-1):
    dl.append(al[i+1]-al[i])
    csum+=abs(dl[-1])

# print(csum)
# print(dl)
for _ in range(q):
    l,r,v=map(int, input().split())
    l-=1
    r-=1
    if l!=0:
        csum-=abs(dl[l-1])
        dl[l-1]+=v
        csum+=abs(dl[l-1])
    if r!=n-1:
        csum-=abs(dl[r])
        dl[r]-=v
        csum+=abs(dl[r])
    print(csum)
    # print(dl)