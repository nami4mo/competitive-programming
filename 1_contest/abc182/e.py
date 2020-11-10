import sys
input = sys.stdin.readline

h,w,n,m = map(int, input().split())

# lights = [ [False]*w for _ in range(h)]
# blocks = [ [False]*w for _ in range(h)]
lbs = [[0]*w for _ in range(h)]
# lbsr = [[0]*h for _ in range(w)]

# lightsr = [ [False]*h for _ in range(w)]
# blocksr = [ [False]*h for _ in range(w)]

for _ in range(n):
    a,b =map(int, input().split())
    lbs[a-1][b-1] = 1
    # lbsr[b-1][a-1] = 1

for _ in range(m):
    c,d =map(int, input().split())
    lbs[c-1][d-1] = -1
    # lbsr[d-1][c-1] = -1

al = [ [False]*w for _ in range(h)]
# alr = [ [False]*w for _ in range(h)]

# cnt = 0
light_flag = False
for hi in range(h):
    hatena_start = 0
    light_flag = False
    row = lbs[hi]
    for wi in range(w):
        if row[wi] == 1:
            al[hi][wi] = True
            if not light_flag:
                for wwi in range(hatena_start,wi):
                    al[hi][wwi] = True
                light_flag = True
                hatena_start = wi
            else:
                hatena_start = wi
        elif row[wi] == -1:
            hatena_start = wi+1
            light_flag = False
        else:
            if light_flag:
                al[hi][wi] = True


light_flag = False
for wi in range(w):
    hatena_start = 0
    light_flag = False
    for hi in range(h):
        if lbs[hi][wi] == 1:
            al[hi][wi] = True
            if not light_flag:
                for hhi in range(hatena_start,hi):
                    al[hhi][wi] = True
                light_flag = True
                hatena_start = hi
            else:
                hatena_start = hi
        elif lbs[hi][wi] == -1:
            hatena_start = hi+1
            light_flag = False
        else:
            if light_flag:
                al[hi][wi] = True

ans = 0
for i in range(h):
    for j in range(w):
        if al[i][j]: ans += 1

print(ans)