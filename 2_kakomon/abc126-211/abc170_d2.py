n=int(input())
al=list(map(int, input().split()))
al.sort()

cntl = []
prev = al[0]
cnt = 1
for a in al[1:]:
    if prev == a: cnt+=1
    else:
        cntl.append((prev,cnt))
        cnt = 1
        prev = a
cntl.append((prev,cnt))

ans=0
used=[False]*(10**6+1)
for num,cnt in cntl:
    if cnt>1:
        if not used[num]:
            cn=num
            while cn<=10**6:
                used[cn]=True
                cn+=num
    else:
        if used[num]:continue
        ans+=1
        cn=num
        while cn<=10**6:
            used[cn]=True
            cn+=num

print(ans)