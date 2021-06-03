s=input()
use=[]
for i in range(10):
    if s[i]=='o':use.append(i)

ans=0
for i in range(0,10000):
    # if i<1000 and s[0]=='x':continue
    ss=str(i).zfill(4)
    ok=True
    for u in use:
        if str(u) not in ss:
            ok=False
            break
    if not ok:continue
    for si in ss:
        if s[int(si)]=='x':
            ok=False
            break
    if not ok:continue
    ans+=1

print(ans)

