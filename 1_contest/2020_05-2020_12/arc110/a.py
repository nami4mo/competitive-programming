def p_factorization_t(n):
    if n == 1: return []
    pf_cnt = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i == 0:
            cnt = 0
            while temp%i == 0:
                cnt += 1
                temp //= i
            pf_cnt.append((i,cnt))

    if temp != 1: pf_cnt.append((temp,1))
    return pf_cnt

n=int(input())
anss = {}

for i in range(2,n+1):
    facs = p_factorization_t(i)
    for k,v in facs:
        if not k in anss:
            anss[k]=v
        else:
            anss[k] = max(anss[k], v)

ans=1
for k,v in anss.items():
    ans *= pow(k,v)

print(ans+1)
