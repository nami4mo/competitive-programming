n,m=map(int, input().split())
dl=list(range(1,n+1))

poped=0
for _ in range(m):
    d=int(input())
    if poped==d:continue
    case=0
    for i in range(n):
        if dl[i]==d:
            case=i
            break
    poped,dl[i]=d,poped

for d in dl:print(d)