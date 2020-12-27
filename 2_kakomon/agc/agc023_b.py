n=int(input())
sl=[]
for _ in range(n):
    row=list(input())
    sl.append(row)

ans=0
for i in range(n):
    new_sl=[]
    for row in sl:
        tmprow=row[(i+1):]+row[0:(i+1)]
        new_sl.append(tmprow)
    ok=True
    for a in range(n):
        for b in range(n):
            if new_sl[a][b]!=new_sl[b][a]:ok=False
    if ok:ans+=n
print(ans)