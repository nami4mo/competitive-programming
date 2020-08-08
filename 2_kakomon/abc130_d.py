N, K = map(int, input().split()) 
al = list(map(int, input().split())) 

ans = 0
curr_sum = al[0]
curr_end = 0
for i in range(len(al)):
    # print('---')
    # print(i)
    while curr_sum < K and curr_end < N-1:
        curr_end += 1
        curr_sum += al[curr_end]
    # print(curr_sum)
    if curr_sum < K: break
    ans += (N-curr_end)
    curr_sum -= al[i]

print(ans)