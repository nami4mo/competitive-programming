s=input()
s=s.replace('10','x')

marks=['S','H','D','C']
ts=['x','J','Q','K','A']
cnts={m:0 for m in marks}

ans=''
for i in range(len(s)//2):
    m=s[i*2]
    n=s[i*2+1]
    if n in ts:cnts[m]+=1
    if cnts[m]==5:
        for t in ts:
            ans=ans.replace(m+t,'')
        break
    ans+=m
    ans+=n
ans=ans.replace('x','10')
if not ans:ans=0
print(ans)