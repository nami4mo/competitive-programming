n,x = map(int, input().split())
al = list(map(int, input().split()))

ans = 0
if al[0] > x:
    ans += (al[0]-x)
    al[0] = x

for i in range(1,n):
    rem = al[i-1]+al[i] - x
    if rem > 0:
        al[i] -= rem
        ans += rem

print(ans)