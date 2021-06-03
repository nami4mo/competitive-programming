n,k=map(int, input().split())
vl=[]
for _ in range(n):
    a,b=map(int, input().split())
    vl.append(a-b)
    vl.append(b)

vl.sort(reverse=True)
ans=sum(vl[:k])
print(ans)