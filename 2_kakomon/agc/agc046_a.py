from math import gcd
x=int(input())
g=gcd(x,360)
l=g*(x//g)*(360//g)
ans=l//x
print(ans)