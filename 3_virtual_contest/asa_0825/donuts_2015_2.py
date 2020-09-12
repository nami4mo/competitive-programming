from itertools import combinations


n,m = map(int, input().split())
al = list(map(int, input().split()))    
combl = []
comb_condl = []
for _ in range(m):
    row = list(map(int, input().split()))
    combl.append(row[0])
    comb_condl.append(row[2:])

ll = list(range(1,n+1))  # list of elements
combinationsl = list(combinations(ll, 9))

ans = 0
for com in combinationsl:
    curr_val = 0
    comset = set(com)
    for c in com:
        curr_val += al[c-1]
    for combv, combcl in zip(combl, comb_condl):
        cnt = 0
        for combc in combcl:
            if combc in comset: 
                cnt += 1
        if cnt >= 3:
            curr_val += combv

    ans = max(ans,curr_val)

print(ans)