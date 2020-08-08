# https://atcoder.jp/contests/atc001/tasks/dfs_a


def search(x,y):
    # print('start', x,y)
    global reached
    if x >= w or y >= h or x < 0 or y < 0 or city[x][y] == '#':
        return
    if reached[x][y]:
        return
    reached[x][y] = True
    # print('ok.......',x,y)
    # print(reached)
    search(x+1,y)
    search(x-1,y)
    search(x,y+1)
    search(x,y-1)


h, w = map(int, input().split()) 

city = []
# reached = [ [False]*w ] * h
reached = [[False for _ in range(w)] for _i in range(h)]

for i in range(h):
    row = list(input())
    if 's' in row:
        s_y, s_x = i, row.index('s')
    if 'g' in row:
        g_y, g_x = i, row.index('g')
    city.append(row)

# print(reached)
search(s_x, s_y)
print(reached)
for row in reached:
    print(row)
print(s_x,s_y)
print(g_x,g_y)

if reached[g_x][g_y]: print('Yes')
else: print('No')



import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right
 
N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
 
neg = bisect_left(A, 0)
pos = bisect_right(A, 0)
 
def less(x):
    res = 0
    b = 0
    for i in range(0, neg):
        while b != N and A[i] * A[b] >= x:
            b += 1
        while b != 0 and A[i] * A[b - 1] < x:
            b -= 1
        res += max(i - b, 0)
    for i in range(neg, pos):
        if x > 0:
            res += i
    for i in range(pos, N):
        while b != N and A[i] * A[b] < x:
            b += 1
        while b != 0 and A[i] * A[b - 1] >= x:
            b -= 1
        res += min(b, i)
    return res
 
l = - (10 ** 18 + 1)
r = - l
while l + 1 < r:
    m = (l + r) // 2
    if less(m) < K:
        l = m
    else:
        r = m
print(l)