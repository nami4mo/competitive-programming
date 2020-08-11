h,w,d = map(int, input().split())
al = []
num_to_xy = [(-1,-1)]*(h*w+1)
for hi in range(h):
    row = list(map(int, input().split()))
    for wi,v in enumerate(row):
        num_to_xy[v] = (hi+1, wi+1)

dist_l = [ [] ]*(d+1)
for start in range(1,d+1):
    dists = [0]
    c_dist = 0
    for i in range(start, h*w-d+1, d):
        x1,y1 = num_to_xy[i]
        x2,y2 = num_to_xy[i+d]
        dist = abs(x2-x1) + abs(y2-y1)
        c_dist += dist
        dists.append(c_dist)
    dist_l[start] = dists


ansl = []
q = int(input())
for _ in range(q):
    l,r = map(int, input().split())
    start = l%d
    if start == 0: start = d
    posl, posr = (l-start)//d, (r-start)//d
    ans = dist_l[start][posr] - dist_l[start][posl]
    ansl.append(ans)

for a in ansl: print(a)