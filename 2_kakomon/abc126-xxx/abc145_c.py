import itertools

n = int(input()) 
p_list = itertools.permutations([x for x in range(n)])

# for p in p_list:
#     print(p)

a_list = []
for i in range(n):
    a_list.append(list(map(int,input().split())))


d_sum = 0
cnt = 0
for p in p_list:
    cnt+=1
    curr_d_sum = 0
    curr_pos = p[0]
    for i in p:
        x_d = a_list[curr_pos][0] - a_list[i][0]
        y_d = a_list[curr_pos][1] - a_list[i][1]
        d = (x_d**2 + y_d**2)**0.5
        curr_d_sum += d
        curr_pos = i
    d_sum += curr_d_sum
print(d_sum/cnt)