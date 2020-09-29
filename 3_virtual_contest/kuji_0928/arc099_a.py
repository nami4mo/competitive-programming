from math import ceil

n,k = map(int, input().split())
al = list(map(int, input().split()))

ans = ceil((n-1)/(k-1))
print(ans)