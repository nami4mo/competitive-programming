# from itertools import product

# n = int(input())

# edge_comb = []
# for i in range(1,n):
#     for j in range(i+1,n+1):
#         edge_comb.append((i,j))


# comb_n = len(edge_comb)
# ite = product(range(2),repeat=comb_n)
# ite = list(ite)
# for it in ite:
#     it = list(it)
#     gl = [ [] for _ in range(n+1) ]
#     for i,v in enumerate(it):
#         if v == 1:
#             edge = edge_comb[i]
#             a,b = edge
#             gl[a].append(b)
#             gl[b].append(a)
    
#     sums = [0]*(n+1)
#     for i in range(n+1):
#         sums[i] = sum(gl[i])
    
#     val = sums[1]
#     for i in range(2,n+1):
#         if sums[i] != val:
#             break
#     else:
#         print(gl)

n = int(input())
gl = [ [] for _ in range(n+1) ]

if n%2 == 0:
    ng = n+1
    for i in range(1,n//2+1):
        for j in range(1,n+1):
            # if i+j != ng:
            if i != j and n+1-i != j:
                gl[i].append(j)
                gl[n+1-i].append(j)
else:
    ng = n
    for i in range(1,n//2+1):
        for j in range(1,n+1):
            if i != j and n-i != j:
                gl[i].append(j)
                gl[n-i].append(j)  
    gl[n] = list(range(1,n))

cnt = 0
for g in gl:
    cnt += len(g)

s = set()
print(cnt//2)
for i,g in enumerate(gl):
    if i == 0: continue
    for v in g:
        if (v,i) in s: continue
        print(i,v)
        s.add((i,v))