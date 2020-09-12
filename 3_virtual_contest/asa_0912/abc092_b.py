n=int(input())
d,x=map(int, input().split())
ans = 0
for _ in range(n):
    a =int(input())
    ans += ((d-1)//a+1)

ans += x
print(ans)