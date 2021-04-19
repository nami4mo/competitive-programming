h,w,m=map(int, input().split())
st=set()
hcnt=[0]*h
wcnt=[0]*w
for _ in range(m):
    h,w=map(int, input().split())
    h-=1
    w-=1
    hcnt[h]+=1
    wcnt[w]+=1
    st.add((h,w))

hc=[(c,i) for i,c in enumerate(hcnt)]
wc=[(c,i) for i,c in enumerate(wcnt)]
hc.sort(reverse=True)
wc.sort(reverse=True)
hma=hc[0][0]
wma=wc[0][0]
ans=hma+wma
for ch,hi in hc:
    if ch!=hma:break
    for cw,wi in wc:
        if cw!=wma:break
        if (hi,wi) not in st:
            print(ans)
            exit()
print(ans-1)