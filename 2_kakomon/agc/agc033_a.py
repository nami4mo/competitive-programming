import sys

def d(pa,pb):
    return abs(pa[0]-pb[0]) + abs(pa[1]-pb[1])

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

h, w = map(int, input().split()) 

b_l = []
for i in range(h):
    a_l = list(input())[:-1]
    for j, v in enumerate(a_l):
        if v == '#':
            b_l.append([i,j])

all_max = 0
n_b = len(b_l)
for i in range(n_b):
    curr_min = 9999
    for j in range(n_b):
        if i == j:continue
        xi,yi = b_l[i][0], b_l[i][1]
        xj,yj = b_l[j][0], b_l[j][1]
        diff = abs(xi-xj) + abs(yi-yj)
        curr_min = min(diff, curr_min)
    all_max = max(all_max, curr_min)


curr_max = 0
for i in range(h):
    p1 = [h,0]
    p2 = [h,w-1]
    