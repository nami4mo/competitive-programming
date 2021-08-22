n = int(input())
a_list = list(map(int, input().split())) 

num_dict = {}
for a in a_list:
    num_dict.setdefault(a,0)
    num_dict[a] += 1

all_comb = 0
for num,cnt in num_dict.items():
    comb = cnt*(cnt-1)//2
    all_comb += comb

for a in a_list:
    a_cnt = num_dict[a]
    a_comb_diff = a_cnt*(a_cnt-1)//2 - (a_cnt-1)*(a_cnt-2)//2
    print(all_comb-a_comb_diff)

