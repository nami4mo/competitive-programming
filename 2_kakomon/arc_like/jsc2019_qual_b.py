n,k = map(int, input().split())
al = list(map(int, input().split()))
inner_invs = [0]*n
outer_invs = [0]*n

for i in range(n):
    inner_cnt = 0
    outer_cnt = 0
    for j in range(n):
        if al[i] > al[j]:
            if i < j:
                inner_cnt += 1
                outer_cnt +=1
            elif i > j:
                outer_cnt += 1
    inner_invs[i] = inner_cnt
    outer_invs[i] = outer_cnt


ans = 0
MOD = 10**9+7

for v in outer_invs:
    ans += v*k*(k-1)//2
    ans %= MOD

for v in inner_invs:
    ans += v*k

print(ans%MOD)
