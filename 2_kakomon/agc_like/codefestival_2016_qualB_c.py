from collections import deque
from heapq import heapify, heappop, heappush
w,h=map(int, input().split())
# wl=[int(input()) for _ in range(w)]
# hl=[int(input()) for _ in range(h)]
el = []
for i in range(w):
    c = int(input())
    el.append((c,'w',i))
for i in range(h):
    c = int(input())
    el.append((c,'h',i))

heapify(el)

hrem = w+1
wrem = h+1
ans = 0
while el:
    c, wh, i = heappop(el)
    if wh=='w':
        ans += c*max(wrem,0)
        hrem-=1
    else:
        ans += c*max(hrem,0)
        wrem-=1

print(ans)
    