N = int(input())
Q = int(input())
ql = []
for _ in range(Q):
    ql.append(list(map(int, input().split())) )


rows = [i for i in range(N)]
cols = [i for i in range(N)]
rev_flg = False

for q in ql:
    if q[0] == 3:
        rev_flg = not rev_flg
    
    else:
        a, b = q[1]-1, q[2]-1
        if (not rev_flg and q[0] == 1) or (rev_flg and q[0] == 2):
            rows[a], rows[b] = rows[b], rows[a]
        elif (not rev_flg and q[0] == 2) or (rev_flg and q[0] == 1):
            cols[a], cols[b] = cols[b], cols[a]
        elif q[0] == 4:
            if rev_flg:
                a,b = b,a
            row = rows[a]+1
            col = cols[b]+1
            ans = N*(row-1)+col-1
            print(ans)
