from collections import deque

n,m = map(int, input().split())
si = input()

s = deque(list(si)[::-1])
# print(s)
s.popleft()
pos = 0
next_max = 0
prev_move = m
ansl = []
while s:
    rem = m-prev_move
    # print(rem)
    for i in range(m-rem):
        poped = s.popleft()
        if poped == '0':
            next_max =  pos + rem + i + 1
        if not s:
            next_max = pos + rem + i + 1
            break
    prev_move = next_max - pos
    if prev_move == 0:
        print(-1)
        exit()
    pos = next_max
    ansl.append(prev_move)

ansl = ansl[::-1]
print(*ansl)