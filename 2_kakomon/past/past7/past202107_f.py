n=int(input())
st=set()
for _ in range(n):
    d,s,t=map(int, input().split())
    for i in range(s,t):
        v=d*24+i
        if v in st:
            print('Yes')
            exit()
        st.add(v)
print('No')