n = int(input())
ans = 0
rem = 0
for _ in range(n):
    a = int(input())
    ans += (a+rem)//2
    if (a+rem)%2 == 1 and a > 0: rem = 1
    else: rem = 0

print(ans)