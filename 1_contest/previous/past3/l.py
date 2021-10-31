import heapq
from collections import deque


n = int(input())
tl = []
for _ in range(n):
    t_list = list(map(int, input().split())) 
    q = deque(t_list[1:])
    tl.append(q)


m = int(input())
a_list = list(map(int, input().split())) 


one_list = []
two_list = []
dic = {}
for i, row in enumerate(tl):
    f = row.popleft() *(-1)
    one_list.append(f)
    dic[f] = i
    if len(row) > 0:
        s = row.popleft() *(-1)
        two_list.append(s)
        dic[s] = i
    
heapq.heapify(one_list)
heapq.heapify(two_list)

for a in a_list:
    if a == 1:
        p = heapq.heappop(one_list)*(-1)
        print(p)
        row = dic[p*(-1)]
        if len(tl[row]) > 0:
            v = tl[row].popleft()
            
            heapq.heappush(two_list, v*(-1))
            heapq.he