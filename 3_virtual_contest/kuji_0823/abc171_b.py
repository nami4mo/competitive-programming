n,k = map(int, input().split())

pl = list(map(int, input().split()))
pl.sort()
ans = sum(pl[:k])
print(ans)