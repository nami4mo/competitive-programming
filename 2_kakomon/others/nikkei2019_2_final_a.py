n=int(input())
al=list(map(int, input().split()))
bl=[0]*n
cl=[0]*n
for i in range(n):
    cnt=0
    for j in range(i):
        if al[j]<al[i]:cnt+=1
    bl[i]=cnt

for i in range(n-1,-1,-1):
    cnt=0
    for j in range(n-1,i,-1):
        if al[i]>al[j]:cnt+=1
    cl[i]=cnt

ans=0
for i in range(n):
    ans+=bl[i]*cl[i]
print(ans)