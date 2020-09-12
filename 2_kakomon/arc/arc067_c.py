def p_factorization(n):
    if n == 1: return {}
    pf_cnt = {}
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i == 0:
            cnt = 0
            while temp%i == 0:
                cnt += 1
                temp //= i
            pf_cnt[i] = cnt

    if temp != 1: pf_cnt[temp] = 1
    return pf_cnt


n = int(input())
pf_cnts = {}
for i in range(2,n+1):
    i_pf_cnt = p_factorization(i)
    for k,v in i_pf_cnt.items():
        pf_cnts.setdefault(k,0)
        pf_cnts[k] += v

MOD = 10**9+7  
ans = 1
for k,v in pf_cnts.items():
    ans *= (v+1)
    ans %= MOD                       

print(ans)