from collections import Counter
s=input()
n=len(s)
ans=n*(n+1)//2+1
c=Counter(s)
alps = 'abcdefghijklmnopqrstuvwxyz'
for a in alps:
    v=c[a]
    ans-=v*(v+1)//2
print(ans)