n = int(input())
ans = 0
for a in range(1,n):
    b_cnt = (n-1)//a
    ans += b_cnt

print(ans)