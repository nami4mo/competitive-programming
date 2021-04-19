n,k=map(int, input().split())
al=list(map(int, input().split()))
asum=sum(al)

divs = []
for i in range(1, int(asum**0.5)+1):
    if asum%i == 0:
        divs.append(i)
        if i*i != asum: divs.append(asum//i)

divs.sort(reverse=True)
# print(divs)

for div in divs:
    rems=[]
    for a in al:
        if a%div!=0:rems.append(a%div)
    rems.sort()
    krem=k
    for i in range(len(rems)):
        if rems[i]==0:
            print(div)
            exit()
        if krem<rems[i]:break
        krem-=rems[i]
        rems[i]=0
    need=0
    for r in rems:
        need+=(div-r)%div
    if need<=k:
        print(div)
        exit()


