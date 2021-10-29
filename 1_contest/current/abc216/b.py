n=int(input())
st=set()
for _ in range(n):
    s,t=map(str, input().split())
    if (s,t) in st:
        print('Yes')
        exit()
    st.add((s,t))
print('No')