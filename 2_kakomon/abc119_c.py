from itertools import product
import bisect

N, A, B, C = map(int, input().split()) 
tl = [C,B,A]

ll = []
for _ in range(N):
    ll.append(int(input()))



ans = 10**8
ite = product(range(4),repeat=N)
for pattern in ite:
    bag = [[],[],[]]
    singles = []
    mp = 0
    for i, p in enumerate(pattern):
        if p == 3: singles.append(ll[i])
        else: bag[p].append(ll[i])
    
    zero_cnt = 0
    for b in bag:
        if not b: zero_cnt+=1
        else: mp += (len(b)-1)*10
    if not singles: zero_cnt+=1
    if zero_cnt >= 2: continue

    bamboos = []
    for b in bag:
        if b: bamboos.append(sum(b))
    for s in singles:
        bamboos.append(s)

    bamboos.sort()
    # print(bamboos)
    
    for t in tl:
        curr_min = 10000
        curr_min_i = 0
        for i, ba in enumerate(bamboos):
            if abs(ba - t) < curr_min:
                curr_min = abs(ba-t)
                curr_min_i = i
        mp += curr_min
        bamboos.pop(curr_min_i)

    ans = min(ans,mp)

print(ans)