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
al=list(map(int, input().split()))
bl=[]
xor=0
for a in al:
    ps=p_factorization_t(a)
    b=0
    for _,v in ps:b+=v
    xor=xor^b
if xor==0:
    print('No')
else:
    print('Yes')