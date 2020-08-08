n, m = map(int, input().split()) 
a_list = []

for i in range(n):
    a_list.append(list(map(int, input().split())) )


p_max = 0
for i in range(m-1):
    for j in range(i+1,m):
        curr_p = 0
        for a_row in a_list:
            p = max(a_row[i], a_row[j])
            curr_p += p
        if curr_p > p_max: p_max = curr_p

print(p_max)