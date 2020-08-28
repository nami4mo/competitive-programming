import math
def com(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

n,p = map(int, input().split())
al = list(map(int, input().split()))

a0 = 0
a1 = 0
for a in al:
    if a%2 == 0:
        a0 += 1
    else:
        a1 += 1

ans = pow(2,a0)
ans2 = 0
if p == 0:
    for i in range(0,51,2):
        if a1 < i:break
        ans2 += com(a1,i)

else:
    for i in range(1,51,2):
        if a1 < i:break
        ans2 += com(a1,i)
print(ans*ans2)