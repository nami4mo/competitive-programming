from itertools import permutations

n,c = map(int, input().split())
cln = list(range(0,c))
cpl = list(permutations(cln,3))

dl = []
for _ in range(c):
    row = list(map(int, input().split()))
    dl.append(row)

cl = []
for _ in range(n):
    row = list(map(int, input().split()))
    cl.append(row)


costs = [ [0]*c for _ in range(3) ]
for i in range(n):
    for j in range(n):
        for target_c in range(c):
            val3 = (i+j+2)%3
            orig_c = cl[i][j]-1
            cost = dl[orig_c][target_c]
            costs[val3][target_c] += cost


ans = 10**10
for cp in cpl:
    cost = costs[0][cp[0]] + costs[1][cp[1]] + costs[2][cp[2]]
    ans = min(ans,cost)

print(ans)