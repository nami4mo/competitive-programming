n,k=map(int, input().split())
v=k//n
rem=k%n
al=list(map(int, input().split()))
ali=[(a,i) for i,a in enumerate(al)]
ali.sort()
ansl=[v]*n
for i in range(rem):
    _,ind=ali[i]
    ansl[ind]+=1

for a in ansl:print(a)