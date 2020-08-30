
n = int(input())
lrl = []
for _ in range(n):
    l,r = map(int, input().split())
    lrl.append((l,r*(-1)))


lrl.sort()
ansil = [0]*n
c_min_max = 0
c_max_min = 10**10
for i in range(n):
    l,r = lrl[i]
    r *= -1
    c_min_max = l
    c_max_min = min(c_max_min,r)
    ans = max(0, c_max_min - c_min_max + 1)
    ansil[i] = ans


ansilr = [0]*n
c_min_max = lrl[-1][0]
c_max_min = 10**10
for i in range(n-1,-1, -1):
    l,r = lrl[i]
    r *= -1
    c_max_min = min(c_max_min, r)
    ans = max(0, c_max_min - c_min_max + 1)
    ansilr[i] = ans

ans = 0
for i in range(n-1):
    one = ansil[i]
    two = ansilr[i+1]
    ans = max(ans, one+two)


for i in range(1,n-1):
    


print(ans)