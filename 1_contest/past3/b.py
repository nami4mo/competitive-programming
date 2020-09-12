n, m, q = map(int, input().split()) 
n_solved = [ [] for _ in range(n+1)]
m_scores = [n]*(m+1)
ql = []
for _ in range(q):
    ql.append(list(map(str, input().split())) )


for qu in ql:
    if qu[0] == '2':
        curr_n = int(qu[1])
        curr_m = int(qu[2])
        n_solved[curr_n].append(curr_m)
        m_scores[curr_m] -= 1
    else:
        curr_n = int(qu[1])
        curr_n_solved = n_solved[curr_n]
        s_sum = 0
        for sol in curr_n_solved:
            s_sum += m_scores[sol]
        print(s_sum)
