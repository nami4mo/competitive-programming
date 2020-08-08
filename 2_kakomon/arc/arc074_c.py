h,w = map(int, input().split())

if h%3 == 0 or w%3 == 0:
    print(0)
    exit()

ans = min(w,h)

for hi in range(1,h):
    top = hi*w
    bottom_big = (h-hi)*((w+1)//2)
    bottom_small = (h-hi)*(w//2)
    smax = max(top,bottom_big)
    smin = min(top,bottom_small)
    ans = min(ans, smax-smin)


for wi in range(1,w):
    top = wi*h
    bottom_big = (w-wi)*((h+1)//2)
    bottom_small = (w-wi)*(h//2)
    smax = max(top,bottom_big)
    smin = min(top,bottom_small)
    ans = min(ans, smax-smin)

print(ans)