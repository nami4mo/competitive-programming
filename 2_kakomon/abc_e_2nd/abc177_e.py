MAX=10**6+1
n=int(input())
al=list(map(int, input().split()))
cnts=[0]*MAX
for a in al:
    cnts[a]+=1

visited=[False]*MAX
for i in range(2,MAX):
    if visited[i]:continue
    cnt=0
    for j in range(i,MAX,i):
        cnt+=cnts[j]
        visited[j]=True
    if cnt>=2:
        break
else:
    print('pairwise coprime')
    exit()
from math import gcd
g=al[0]
for a in al: g=gcd(g,a)
if g==1:
    print('setwise coprime')
else:
    print('not coprime')