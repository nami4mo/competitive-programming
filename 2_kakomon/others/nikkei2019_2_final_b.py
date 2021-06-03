s=input()
n=len(s)

s='a'*500
n=500
ans=0
loop=0
for l3 in range(n):
    for r4 in range(l3+2,n,2):
        n34=(r4-l3)//2
        if s[l3:l3+n34]!=s[l3+n34:r4]: continue
        rrem=n-r4
        for l2 in range(1,l3):
            loop+=1
            n26=l3-l2
            if rrem-1<n26:continue
            if s[l2:l3]==s[-n26:]:ans+=1
print(ans)