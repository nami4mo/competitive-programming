from collections import deque

n = int(input())
al = list(map(int, input().split()))
asum = sum(al)

first_q = al[1:n:2]
last_ind = n-2
curr_sum = sum(first_q)
q = deque(first_q)


ans = [0]*n
ans[0] = asum - curr_sum*2
for i in range(2,n,2):
    next_ind = (last_ind+2)%n
    next_a = al[next_ind]
    poped_a = q.popleft()
    curr_sum -= poped_a
    curr_sum += next_a
    ans[i] = asum - curr_sum*2
    last_ind = next_ind


first_q = al[2:n:2]
last_ind = n-1
curr_sum = sum(first_q)
q = deque(first_q)
ans[1] = asum - curr_sum*2
for i in range(3,n,2):
    next_ind = (last_ind+2)%n
    next_a = al[next_ind]
    poped_a = q.popleft()
    curr_sum -= poped_a
    curr_sum += next_a
    ans[i] = asum - curr_sum*2
    last_ind = next_ind

print(*ans)