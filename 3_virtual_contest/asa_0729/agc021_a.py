n = input()
n_len = len(n)

ans = 0
for i in range(n_len+1):
    curr_sum = 0
    for j in range(n_len):
        num = int(n[j])
        if j < i:
            curr_sum += num
        elif j == i:
            if num == 0: curr_sum = -10000000000
            curr_sum += (num-1)
        else:
            curr_sum += 9
    ans = max(ans, curr_sum)

print(ans)