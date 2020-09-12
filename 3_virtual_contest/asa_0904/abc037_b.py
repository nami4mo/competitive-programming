n,q = map(int, input().split())
al = [0]*n
for _ in range(q):
    l,r,t = map(int, input().split())
    for i in range(l,r+1):
        al[i-1] = t

print(*al)