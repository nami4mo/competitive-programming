n = int(input())    
spl = []
for i in range(n):
    s,p = map(str, input().split())
    p = int(p) *(-1)
    spl.append((s,p,i+1))
    
spl.sort()
for s,p,i in spl:
    print(i)