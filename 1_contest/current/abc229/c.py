n,w=map(int, input().split())
abl=[]
for _ in range(n):
    a,b=map(int, input().split())
    abl.append((a,b))

abl.sort(reverse=True)
ans=0
rem=w
for a,b in abl:
    if rem>b:
        ans+=a*b
        rem-=b
    else:
        ans+=a*rem
        break
print(ans)