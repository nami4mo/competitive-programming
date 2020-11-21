from math import factorial

n,k = map(int, input().split())
v = factorial(n)//k

rems = list(range(1,n+1))
for i in range(n,0,-1):
    rem_cnt = factorial(i-1)
    order = (v-1)//rem_cnt
    ans = rems[order]
    print(ans)
    v%=rem_cnt
    if v == 0: 
        v = rem_cnt
    next_rems = []
    for r in rems:
        if r != ans: next_rems.append(r)
    rems = next_rems[:]

