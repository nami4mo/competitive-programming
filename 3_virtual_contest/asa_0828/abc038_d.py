# from collections import deque
import bisect



n=int(input())
# abl_r=[tuple(map(int, input().split())) for _ in range(n)]
abl_r = []
for _ in range(n):
    a,b = map(int, input().split())
    abl_r.append((a,-b))
abl_r.sort()

bl = []
for a,b in abl_r:
    bl.append(b*(-1))
# prev_a = -1
# prev_max_b = 0
# for a,b in ablraw:
#     if prev_a == a:
#         bl[-1] = b
#     else:
#         bl.append(b)
#     prev_a = a
#     prev_max_b = b


# print(bl)

# print(bl)
lis = [bl[0]]
for i in range(len(bl)):
    if bl[i] > lis[-1]:
        lis.append(bl[i])
    else:
        lis[bisect.bisect_left(lis, bl[i])] = bl[i]

print(len(lis))

# q = deque([(0,0)])
# for b in bl:
#     new_q = deque([])
#     while q:
#         minv, cnt = q.pop()
#         if b > minv:
#             new_q.append((b,cnt+1))
#         new_q.append((minv,cnt))


