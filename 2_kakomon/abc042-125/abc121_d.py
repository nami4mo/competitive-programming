def get_one_cnts(n):
    one_cnts_dic = []
    for i in range(0,40): 
        if i == 0:
            if n%4 in [1,2]:
                one_cnts_dic.append(1)
            else:
                one_cnts_dic.append(0)
        else:
            cycle = 2**(i+1) 
            if n%cycle in range(cycle//2, cycle, 2):
                one_cnts_dic.append(1)
            else:
                one_cnts_dic.append(0)
    return one_cnts_dic

a,b = map(int, input().split())
a_one_cnts = get_one_cnts(a-1)
b_one_cnts = get_one_cnts(b)
# print(a_one_cnts)
# print(b_one_cnts)
ans = 0
for i in range(40):
    if a_one_cnts[i] ^ b_one_cnts[i]:
        ans += 2**i

print(ans)