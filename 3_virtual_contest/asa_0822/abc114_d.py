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
pd = {}
for i in range(1,n+1):
    curr_p = p_factorization(i)
    for p,cnt in curr_p.items():
        pd.setdefault(p,0)
        pd[p] += cnt

ans = 0

cnt3 = 0
cnt5 = 0
cnt15 = 0
cnt25 = 0
cnt75 = 0

for v in pd.values():
    if v >= 74: cnt75 += 1
    if v >= 24: cnt25 += 1
    if v >= 14: cnt15 += 1
    if v >= 4: cnt5 += 1
    if v >= 2: cnt3 += 1


ans += cnt75
ans += max(cnt15*(cnt5-1), 0)
ans += max(0,cnt25*(cnt3-1))
ans += max(0,(cnt3-2)*(cnt5)*(cnt5-1)//2)
print(ans)