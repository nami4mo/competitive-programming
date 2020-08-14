from itertools import product

n,m,x = map(int, input().split())

al = []
cl = []
for _ in range(n):
    row = list(map(int, input().split())) 
    cl.append(row[0])
    al.append(row[1:])


ans = 10**9
bit = 2
ite = list(product(range(bit),repeat=n))
for pattern in ite:
    skills = [0]*m
    cost = 0
    for i, v in enumerate(pattern):
        if v == 1:
            curr_al = al[i]
            cost += cl[i]
            for j, a in enumerate(curr_al):
                skills[j] += a
    if min(skills) >= x:
        ans = min(ans,cost)

if ans == 10**9: ans = -1
print(ans)