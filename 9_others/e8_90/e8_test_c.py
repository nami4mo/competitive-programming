n=int(input())
st=set()
for i in range(1,n+1):
    st.add(i**2)

ans=0
for x in range(1,n+1):
    y2=n**2-x**2
    if y2 in st:ans+=1
print(ans)