n,a,b = map(int, input().split())

loop = a+b
l_cnt = n//loop
rem = n%loop

ans = l_cnt*a
if rem < a:
    ans += rem
else:
    ans += a

print(ans)