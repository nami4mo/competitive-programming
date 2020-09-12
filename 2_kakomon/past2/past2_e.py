n = int(input())
a_list = list(map(int, input().split())) 

res = []
for i in range(n):
    curr_i = i + 1
    cnt = 0
    while True:
        cnt += 1
        curr_i = a_list[curr_i-1]
        # print(curr_i)
        if curr_i == i+1:
            break
    res.append(cnt)
print(*res)
