h,w,k = map(int, input().split())
S = []
for _ in range(h):
    S.append(list(input()))

ans = [[0]*w for _ in range(h)]
ans = []
first_row_flag = True
first_row_cnt = 0
curr_num = 1
for i in range(h):
    row = []
    curr_s_row = S[i]
    if '#' in S[i]:
        ichigo = 0
        for j in range(w):
            if curr_s_row[j] == '#':
                ichigo += 1
                if ichigo >= 2: curr_num += 1
            row.append(curr_num)

        
        curr_num += 1
        
        if first_row_flag:
            first_row_flag = False
            for j in range(first_row_cnt):
                ans.append(row)
        ans.append(row)
    
    else:
        if first_row_flag:
            first_row_cnt+=1
        else:
            ans.append(ans[-1])

for row in ans:
    print(*row)