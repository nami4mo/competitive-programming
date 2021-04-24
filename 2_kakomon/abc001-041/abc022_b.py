n=int(input())
st=set()
ans=0
for _ in range(n):
    a=int(input())
    if a in st:ans+=1
    st.add(a)
print(ans)