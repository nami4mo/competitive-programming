# 60 -> {2:2, 3:1, 5:1}
def factorization(n):
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
    if not pf_cnt: pf_cnt[n] = 1

    return pf_cnt


n = int(input())
prime_cnts = {}
for i in range(1,n+1):
    fac = factorization(i)
    for prime, cnt in fac.items():
        prime_cnts.setdefault(prime, 0)
        prime_cnts[prime] += cnt


cnt_74 = 0
cnt_24 = 0
cnt_14 = 0
cnt_4 = 0
cnt_2 = 0
for prime, cnt in prime_cnts.items():
    if cnt >= 74:
        cnt_74 += 1
    if cnt >= 24:
        cnt_24 += 1
    if cnt >= 14:
        cnt_14 += 1
    if cnt >= 4:
        cnt_4 += 1
    if cnt >= 2:
        cnt_2 += 1

ans = 0
ans += cnt_74
ans += cnt_14*(cnt_4-1)
ans += cnt_24*(cnt_2-1)
ans += (cnt_2-2) * cnt_4*(cnt_4-1)//2
print(ans)