n=int(input())
al=list(map(int, input().split()))
al.sort()
d=al[-1]
if al[0]!=(d+1)//2:
    print('Impossible')
    exit()

from collections import Counter
c=Counter(al)

if d%2==0 and c[(d+1)//2]!=1:
    print('Impossible')
    exit()
if d%2==1 and c[(d+1)//2]!=2:
    print('Impossible')
    exit()

for i in range((d+1)//2+1,d+1):
    if c[i]<2:
        print('Impossible')
        exit()
print('Possible')