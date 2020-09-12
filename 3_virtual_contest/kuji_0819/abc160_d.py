n,x,y = map(int, input().split())

ans = [0]*n
for i in range(1,n):
    for j in range(i+1,n+1):
        v1 = j-i
        v2 = abs(x-i) + 1 + abs(y-j)
        v3 = abs(y-i) + 1 + abs(x-j)
        minv = min(v1,v2,v3)
        ans[minv] += 1

for a in ans[1:]:
    print(a)