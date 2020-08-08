n,k = map(int, input().split()) 
a_list = list(map(int, input().split())) 

min_cost = 10**15
for i in range(2 ** n):
    see_a_ids = []
    for j in range(n):
        if ((i >> j) & 1):
            see_a_ids.append(j)
    
    if len(see_a_ids) < k:
        continue

    curr_max_h = 0
    curr_cost = 0
    for a_i in range(n):
        if a_i in see_a_ids:
            if a_list[a_i] <= curr_max_h:
                h_plus = curr_max_h + 1 - a_list[a_i]
                curr_cost += h_plus
                curr_max_h = curr_max_h+1
            else:
                curr_max_h = a_list[a_i]
        else:
            curr_max_h = max(curr_max_h, a_list[a_i])
    min_cost = min(min_cost, curr_cost)
print(min_cost)