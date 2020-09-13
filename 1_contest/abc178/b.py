a,b,c,d = map(int, input().split())

ans = max(a*c,a*d,b*c,b*d)
if a*b <= 0 or c*d <= 0:
    ans = max(0,ans)

print(ans)

# if b>=0 and d>= 0:
#     ans = b*d
# elif b < 0 and d >= 0:
#     if c <= 0: ans = max(ans,0)
#     else: ans = b*c
# elif b >= 0 and d < 0:
#     if a <= 0: ans = 0
#     else: ans = a*d
# else:
#     ans = a*c

# if a <= 0 and c <= 0:
#     ans = max(ans,a*c)

# print(ans)