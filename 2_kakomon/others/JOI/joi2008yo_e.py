import numpy as np

def r01(n):
    if n == 0:
        return 1
    else:
        return 0

r,c = map(int, input().split()) 
a_list = []
a_list_r = []
for i in range(r):
    row = list(map(int, input().split())) 
    a_list.append(row)
    a_list_r.append([ r01(a) for a in row ])

# print(a_list)
# print(a_list_r)

cnt_max = 0
for i in range(2 ** r):
    a_r_list = []
    for j in range(r):
        if ((i >> j) & 1):
            row = a_list_r[j]
            a_r_list.append(row)
        else:
            row = a_list[j]
            a_r_list.append(row)

    np_a_r = np.array(a_r_list)
    row_sums = np.sum(np_a_r, axis=0)
    row_sums = np.where(row_sums >= r/2, r-row_sums, row_sums)
    cnt = np.sum(row_sums)

    ##  slow...
    # row_sums = list(row_sums)
    # cnt = 0
    # for row_sum in row_sums:
    #     if row_sum >= r/2:
    #         cnt += (r-row_sum)
    #     else:
    #         cnt += row_sum


    zero_cnt = r*c-cnt
    cnt_max = max(cnt_max, zero_cnt)
print(cnt_max)