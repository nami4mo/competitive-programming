n,x = map(int, input().split())
al = list(map(int, input().split()))

costs = al[:]
curr_sums = sum(costs)

# curr_mins = al[:]
curr_mins = al[:]

ans = 10**18
for i in range(0,n): # move cnt
    curr_i_ans = 0
    for j in range(n): # ind
        ind = j-i
        if ind < 0: ind+=n
        # xcost = i*x
        next_a = al[ind]
        if curr_mins[j] > next_a:
            curr_mins[j] = next_a
        cost = curr_mins[j]
        curr_i_ans += cost
    ans = min(ans, curr_i_ans+i*x)

print(ans)