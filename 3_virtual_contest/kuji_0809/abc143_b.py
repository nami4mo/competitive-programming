n = int(input())
dl = list(map(int, input().split()))

ans = 0
for i in range(n-1):
    for j in range(i+1,n):
        ans += dl[i]*dl[j]

print(ans)