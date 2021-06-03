s=input()
s=s.split()
st=set()
for si in s:
    ssi=si.split('@')
    if len(ssi)==0:continue
    for v in ssi[1:]:
        if len(v)>0:st.add(v)

ans=list(st)
ans.sort()
for a in ans:print(a)