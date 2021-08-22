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


n,m=map(int, input().split())
al=list(map(int, input().split()))
st=set()
for a in al:
    pf=p_factorization_t(a)
    for p,_ in pf:
        st.add(p)

ps=list(st)
ps.sort()

ok=[True]*(m+1)
for p in ps:
    # print(p)
    v=p
    while v<=m:
        ok[v]=False
        v+=p
ans=[]
for i in range(1,m+1):
    if ok[i]:ans.append(i)
print(len(ans))
for a in ans:print(a)