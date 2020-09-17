s,c = map(int, input().split())

if s*2 >= c:
    print(c//2)
else:
    ans = s
    rem = c-s*2
    ans += rem//4
    print(ans)