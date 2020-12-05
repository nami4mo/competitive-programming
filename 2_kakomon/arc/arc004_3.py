from math import gcd

x,y=map(int, input().split('/'))
g=gcd(x,y)
x//=g
y//=g
v = int(2*x/y)
cand = [v-1,v,v+1]

ansl = []
for n in cand:
    if n <= 1:continue
    if n%y != 0: continue
    top_bai = n//y
    top = x*top_bai
    diff = n*(n+1)//2-top
    if 1 <= diff <= n:
        ansl.append((n,diff))

for n,d in ansl:
    print(n,d)
if not ansl:
    print('Impossible')