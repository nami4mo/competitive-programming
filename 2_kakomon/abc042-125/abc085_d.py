import math

n,h = map(int, input().split())
al = []
bl = []
for _ in range(n):
    a,b = map(int, input().split())
    al.append((a,'swing'))
    bl.append((b,'throw'))

abl = al + bl
abl.sort(reverse=True)

remain_h = h
ans = 0
for v in abl:
    damage, command = v
    if command == 'swing':
        ans += math.ceil(remain_h/damage)
        break
    else:
        ans += 1
        remain_h -= damage
        if remain_h <= 0:
            break

print(ans)