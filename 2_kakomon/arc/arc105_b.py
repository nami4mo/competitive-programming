from math import gcd

n = int(input())
al = list(map(int, input().split()))

v = al[0]
for a in al[1:]:
    v = gcd(v,a)

print(v)