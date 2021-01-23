n,k,q=map(int, input().split())
al=list(map(int, input().split()))

ans=10**10
for mina in al:
    # chunks=[]
    c_chunk=[]
    avails=[]
    for a in al:
        if a>=mina:
            c_chunk.append(a)
        else:
            c_chunk.sort()
            cnt=len(c_chunk)-k+1
            if cnt>0:
                for c in c_chunk[:cnt]: avails.append(c)
            c_chunk=[]
    c_chunk.sort()
    cnt=len(c_chunk)-k+1
    if cnt>0:
        for c in c_chunk[:cnt]: avails.append(c)
    # print(c_chunk)
    if len(avails)<q: continue
    avails.sort()
    v=avails[q-1]-mina
    ans=min(ans,v)
print(ans)