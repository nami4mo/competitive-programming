import heapq

X, Y, A, B, C = map(int, input().split()) 
pl = list(map(int, input().split())) 
ql = list(map(int, input().split())) 
rl = list(map(int, input().split())) 

pl.sort()
ql.sort()
rl.sort(reverse=True)
pl_x_larges = pl[A-X:A]
ql_y_larges = ql[B-Y:B]

pq_xy = pl_x_larges + ql_y_larges
pq_xy.sort()

for i, r in enumerate(rl):
    if r > pq_xy[i]:
        pq_xy[i] = r
    else:
        break

print(sum(pq_xy))