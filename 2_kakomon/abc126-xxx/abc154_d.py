from collections import deque

n, k = map(int, input().split()) 

p_l = list(map(int, input().split())) 
p_sum_k_l = []

q = deque([])
first_sum = 0
for i in range(k):
    ex = (p_l[i]+1)/2
    q.append(ex)
    first_sum += ex

p_sum_k_l.append(first_sum)
# print(q)

for i in range(k, len(p_l)):
    # print('---')
    poped = q.popleft()
    added = (p_l[i]+1)/2
    # print(poped, added)
    diff = added-poped
    # print(diff)
    next_sum = p_sum_k_l[-1] + diff
    p_sum_k_l.append(next_sum)
    q.append(added)

print(max(p_sum_k_l))