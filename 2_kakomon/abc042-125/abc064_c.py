n=int(input())
al=list(map(int, input().split()))
cnts=[0]*10
cf=0
for a in al:
    if a>=3200:cf+=1
    else:
        cnts[a//400]+=1

cs=0
for c in cnts:
    if c>0: cs+=1

if cs==0:
    print(1,cf)
else:
    print(cs,cs+cf)