H, W, K = map(int, input().split()) 
sl = []
for _ in range(H):
    sl.append(list(input()))


ans = 10**8
for i in range(2 ** (H-1)):
    fail_flag = False
    comb = []
    for j in range(H-1):
        if ((i >> j) & 1): 
            comb.append(j)
    comb.append(H-1)
    # print(comb)
    sections = []
    for k in range(0,len(comb)):
        if k == 0:
            sections.append( sl[0:comb[0]+1] )
        else:
            sections.append( sl[comb[k-1]+1:comb[k]+1] )
    # print(sections)

    partition_cnt = 0
    sections_w_cnts = [0]*len(sections)
    for w in range(W):
        sections_curr_w_cnts = [0]*len(sections)
        partition_flag = False
        for i, sec in enumerate(sections):
            for row in sec:
                if row[w] == '1':
                    sections_curr_w_cnts[i] += 1
                    sections_w_cnts[i] += 1
                    if sections_curr_w_cnts[i] > K:
                        fail_flag = True
                        break
                    if sections_w_cnts[i] > K:
                        partition_flag = True

            if fail_flag: break
        if fail_flag: break

        if partition_flag:
            sections_w_cnts = [v for v in sections_curr_w_cnts]
            # sections_w_cnts[:] = sections_curr_w_cnts[:]
            partition_cnt += 1
        

    if not fail_flag:
        ans = min(len(comb)-1+partition_cnt, ans)

print(ans)