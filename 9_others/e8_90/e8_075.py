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
ps=p_factorization_t(n)
v=0
for _,c in ps:v+=c
ans=0
while v>1:
    v+=1
    v//=2
    ans+=1
print(ans)