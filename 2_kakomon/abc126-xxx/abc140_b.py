n = int(input())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
cl = list(map(int, input().split()))

ans = 0
prev = -2
for a in al:
    ind = a-1
    ans += bl[ind]
    if prev+1 == ind:
        ans += cl[prev]
    prev = ind
print(ans)