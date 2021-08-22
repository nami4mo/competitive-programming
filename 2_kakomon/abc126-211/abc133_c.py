l,r = map(int, input().split())

right = min(r+1, l+2019)
ans = 2019
for i in range(l, right):
    for j in range(i+1, right):
        rem = (i*j)%2019
        ans = min(ans, rem)

print(ans)