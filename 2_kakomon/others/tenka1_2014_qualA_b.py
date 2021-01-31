s=input()
comb=0
adamage=10
bdamage=50
kabu=5
ans=0
tame=False

n=len(s)
events=[ [] for _ in range(n+100)]
for i,si in enumerate(s):
    for e in events[i]:
        if e[0]=='kabu':
            kabu+=e[1]
        elif e[0]=='comb':
            pcomb=comb
            comb+=e[1]
            if comb//10-pcomb//10==1:
                adamage+=1
                bdamage+=5
        elif e[0]=='tame':
            tame=False
    if si=='N':
        if kabu==0 or tame:continue
        ans+=adamage
        events[i+2].append(('comb',1))
        events[i+7].append(('kabu',1))
        kabu-=1
    elif si=='C':
        if kabu<3 or tame:continue
        ans+=bdamage
        tame=True
        events[i+3].append(('tame',0))
        events[i+4].append(('comb',1))
        events[i+9].append(('kabu',3))
        kabu-=3

print(ans)