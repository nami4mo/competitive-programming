n=int(input())
st=set()
for i in range(2,10**5+1):
    if i in st: continue
    v=i
    for j in range(100):
        v*=i
        if v>n: break
        st.add(v)

ok=len(st)
ans=n-ok
print(ans)