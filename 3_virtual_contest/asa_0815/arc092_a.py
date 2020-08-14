n = int(input())
rl = []
bl = []
xs = [(-1,'',False)]*(2*n)
for _ in range(n):
    a,b = map(int, input().split())
    rl.append((a,b))
    xs[a] = (b,'r',False)


for _ in range(n):
    c,d = map(int, input().split())
    bl.append((c,d))
    xs[c] = (d,'b',False)

rl.sort(reverse=True)
bl.sort()

ans = 0
for rx,ry in rl:
    min_x,min_y = 10**5,10**5
    for x in range(rx,2*n):
        y,color,used = xs[x]
        if y > ry and color =='b' and not used and min_y > y:
            min_x = x
            min_y = y
    if min_x != 10**5:
        ans += 1
        xs[min_x] = (min_y,'b',True)

print(ans)