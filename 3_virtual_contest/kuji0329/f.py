n,k=map(int, input().split())
al=list(map(int, input().split()))
asum=sum(al)

divs = []
for i in range(1, int(asum**0.5)+1):
    if asum%i == 0:
        divs.append(i)
        if i*i != asum: divs.append(asum//i)

divs.sort(reverse=True)

for d in divs:
    rems=[]
    for a in al:
        r=a%d
        if r!=0:rems.append(r)
    rn=len(rems)
    rems.sort()
    kr=k
    ksum=0
    back_start=-1
    for i,r in enumerate(rems):
        if kr<r:
            back_start=i
            break
        kr-=r
        ksum+=r
    if back_start==-1:
        print(d)
        exit()
    
    brems=0
    for r in rems[back_start:]:
        brems+=(d-r)
    if ksum>=brems:
        print(d)
        exit()
    
