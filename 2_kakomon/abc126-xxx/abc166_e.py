
n = int(input())
al = list(map(int, input().split()))

ans = 0
i_plus_h_dic = {}

for i, a in enumerate(al):
    input_val = a+i
    i_plus_h_dic.setdefault(input_val,0)
    i_plus_h_dic[input_val] += 1

    comp_val = i - a
    if comp_val in i_plus_h_dic:
        ans += i_plus_h_dic[comp_val]


print(ans)