n,m=map(int, input().split())
cnts=[0]*n
for _ in range(m):
    a,b=map(int, input().split())
    a-=1
    b-=1
    cnts[max(a,b)]+=1
ans=0
for c in cnts:
    if c==1:ans+=1
print(ans)