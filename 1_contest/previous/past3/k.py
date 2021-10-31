N, Q = map(int, input().split()) 
ql = []
for _ in range(Q):
    ql.append(list(map(int, input().split())) )

f_tops = [i for i in range(N+1)]
con_belows = [-1] * (N+1)

for q in ql:
    f,t,x = q[0],q[1],q[2]
    tmp = f_tops[t]
    f_tops[t] = f_tops[f]
    f_tops[f] = con_belows[x]
    con_belows[x] = tmp

desks = [0] * (N+1)
for i in range(1,N+1):
    curr_con = f_tops[i]
    while curr_con != -1:
        # desks[i].append(curr_con)
        desks[curr_con] = i
        curr_con = con_belows[curr_con]

for d in desks[1:]:
    print(d)