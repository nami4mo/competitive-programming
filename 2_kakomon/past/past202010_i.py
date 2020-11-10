n = int(input())
al = list(map(int, input().split()))
alsum = sum(al)

l = 0
r = 0
csum = 0
ans = 10**10
loop = False
while True:
    if csum > alsum/2:
        csum -= al[l]
        l += 1
        if l == n-1: loop = True
    else:
        csum += al[r%n]
        r += 1
    d = abs(alsum-csum-csum)
    ans = min(ans,d)
    if loop and l > 0:
        break
    # print(l,r,csum)

print(ans)
