n,k,s = map(int, input().split())

ans = []
if s == 10**9:
    for i in range(k):
        ans.append(10**9)
    for i in range(n-k):
        ans.append(1)

else:
    for i in range(k):
        ans.append(s)
    for i in range(n-k):
        ans.append(s+1)

print(*ans)