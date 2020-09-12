n,k = map(int, input().split())

cnt_l = [0]*(k+1)
MOD = 10**9+7

for i in range(k,0,-1):
    multi_cnt = k//i
    cnt = pow(multi_cnt,n,MOD)
    
    i_multi = i+i
    while i_multi <= k:
        cnt -= cnt_l[i_multi]
        i_multi+=i

    cnt_l[i] = cnt%MOD

ans = 0
for i, cnt in enumerate(cnt_l):
    ans += i*cnt
    ans %= MOD

# print(cnt_l)
print(ans)