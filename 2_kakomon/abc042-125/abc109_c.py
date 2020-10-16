from math import gcd

n,x = map(int, input().split())
xl = list(map(int, input().split()))
xl = [abs(v-x) for v in xl]

v = xl[0]
for val in xl[1:]:
    v = gcd(v,val)

print(v)