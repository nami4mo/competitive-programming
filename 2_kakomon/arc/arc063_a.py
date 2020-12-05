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

print(len(cntl)-1)