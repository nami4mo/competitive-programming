h,w=map(int, input().split())
pl=[list(map(int, input().split())) for _ in range(h)]

ans=0
for i in range(1,1<<h):
    hl=[]
    for j in range(h):
        if i&(1<<j): hl.append(j)

    cnts={}
    for col in range(w):
        num=pl[hl[0]][col]
        for row in hl:
            if pl[row][col]!=num:break
        else:
            cnts.setdefault(num,0)
            cnts[num]+=1
    
    hlen=len(hl)
    for v in cnts.values():
        ans=max(ans, hlen*v)
print(ans)