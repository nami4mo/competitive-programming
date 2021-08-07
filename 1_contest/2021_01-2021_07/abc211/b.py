st=set()
for _ in range(4):
    s=input()
    if s in st:
        print('No')
        exit()
    st.add(s)
print('Yes')