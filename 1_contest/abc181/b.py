n = int(input())
ans = 0
for _ in range(n):
    a,b = map(int, input().split())
    v = (b-a+1)*(a+b)//2
    ans += v
print(ans)