from math import gcd

n=int(input())
al=list(map(int, input().split()))
amin=min(al)
divs={}
for a in al:
    for d in range(1,int(a**0.5)+1):
        if a%d==0:
            if d not in divs:
                divs[d]=a
            else:
                divs[d]=gcd(divs[d],a)
            if d*d!=a:
                d2=a//d
                if d2 not in divs:
                    divs[d2]=a
                else:
                    divs[d2]=gcd(divs[d2],a)

ans=1
for k,v in divs.items():
    if k>=amin:continue
    if v==k:
        ans+=1

print(ans)
# print(divs)