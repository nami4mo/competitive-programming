n=int(input())
al=list(map(int, input().split()))
bl=list(map(int, input().split()))

def check(al,bl,v):
    d={}
    for b in bl:
        d.setdefault(b,0)
        d[b]+=1
    for a in al:
        c=v^a
        if (not c in d) or d[c]==0:break
        d[c]-=1
    else:
        return True
    return False

ans=set()
for a in al:
    v=a^bl[0]
    if check(al,bl,v):ans.add(v)

ans=list(ans)
ans.sort()
print(len(ans))
for a in ans:print(a)