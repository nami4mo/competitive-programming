al=list(input())
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

ans=''
for c,v in cntl:
    ans+=c
    ans+=str(v)
print(ans)