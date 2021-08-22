n,m = map(int, input().split())
num_cnts = []
al = list(map(int, input().split()))
for a in al:
    num_cnts.append((a,1))

for _ in range(m):
    b,c = map(int, input().split())
    num_cnts.append((c,b))

num_cnts.sort(reverse=True)
ans = 0
curr_cnt = 0
for num,cnt in num_cnts:
    if curr_cnt + cnt <= n:
        ans += num*cnt
        curr_cnt += cnt
    else:
        rem = n-curr_cnt
        ans += rem*num
        break

print(ans)