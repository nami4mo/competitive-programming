k,n,m=map(int, input().split())
al=list(map(int, input().split()))
bl=[]
rems=[]
mrem=m
for i,a in enumerate(al):
    top=a*m
    bottom=n
    val=top//bottom
    rem=top%bottom
    bl.append(val)
    rems.append((rem,i))
    mrem-=val

rems.sort(reverse=True)
for i in range(mrem):
    bl[rems[i][1]]+=1

print(*bl)