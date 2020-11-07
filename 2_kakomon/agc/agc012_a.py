n = int(input())
al = list(map(int, input().split()))
al.sort(reverse=True)
ans = 0
for i in range(n):
    ans += al[i*2+1]
print(ans)