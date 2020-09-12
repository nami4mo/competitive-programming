n,m = map(int, input().split())
imos = [0]*(n+2)

for _ in range(m):
    l,r = map(int, input().split())
    imos[l]+=1
    imos[r+1]-=1

curr_cnt = 0
ans = 0
for i in range(n+1):
    curr_cnt += imos[i]
    if curr_cnt == m: ans += 1

print(ans)