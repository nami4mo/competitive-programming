n,m = map(int, input().split())
xl = list(map(int, input().split()))
yl = list(map(int, input().split()))

xdl = []
ydl = []
for x2,x1 in zip(xl[1:],xl[:-1]):
    xdl.append(x2-x1)

for y2,y1 in zip(yl[1:],yl[:-1]):
    ydl.append(y2-y1)


MOD = 10**9+7
ys = 0
for i,d in enumerate(xdl):
    pattern = (i+1)*(n-1-i)
    ys += pattern*d
    ys%=MOD

# print(ys)
ans = 0

for i,d in enumerate(ydl):
    pattern = (i+1)*(m-1-i)
    ans += pattern*ys*d
    ans%=MOD

print(ans)