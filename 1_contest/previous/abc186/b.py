h,w=map(int, input().split())
al = []
csum=0
m=10**10
for _ in range(h):
    row=list(map(int, input().split()))
    csum+=sum(row)
    m = min(m,min(row))

last=m*h*w
ans = csum-last
print(ans)