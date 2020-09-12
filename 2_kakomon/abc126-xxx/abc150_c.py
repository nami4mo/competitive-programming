import itertools

n = int(input())
p_list = list(map(int,input().split()))
q_list = list(map(int,input().split()))

per_list = itertools.permutations([x+1 for x in range(n)])

p_dict_i = -1
q_dict_i = -1
for dict_i, per in enumerate(per_list):
    p_flg = True
    for i, num in enumerate(per):
        if num != p_list[i]:
            p_flg = False
            break
    q_flg = True
    for i, num in enumerate(per):
        if num != q_list[i]:
            q_flg = False
            break
    if p_flg: p_dict_i = dict_i
    if q_flg: q_dict_i = dict_i

print(abs(p_dict_i-q_dict_i))