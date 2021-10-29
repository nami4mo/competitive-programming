v=['ABC' , 'ARC' , 'AGC' , 'AHC']
st=set()
for _ in range(3):
    s=input()
    st.add(s)

for vv in v:
    if vv not in st:
        print(vv)