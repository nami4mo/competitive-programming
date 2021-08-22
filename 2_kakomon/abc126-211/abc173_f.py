n = int(input())
ss = 0
es = 0
for i in range(1,n+1): ss+=i*(i+1)//2
for i in range(n-1):
    u,v = map(int, input().split())
    if u > v: u,v = v,u
    es += u*(n-v+1)
print(ss-es)