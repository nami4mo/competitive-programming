n,k=map(int, input().split())
cnts=[k]*n
st=set()
for i in range(k):
    c,k=map(str, input().split())
    k=int(k)
    k-=1
    st.add(k)
    if c=='L':
        # cnts[k]=1
        for j in range(k):
            cnts[j]=max(cnts[j]-1,1)
    if c=='R':
        # cnts[k]=1
        for j in range(k,n):
            cnts[j]=max(cnts[j]-1,1)

ans=1
MOD=998244353
for i,c in enumerate(cnts):
    if i in st:continue
    ans*=c
    ans%=MOD
print(ans)       
# print(cnts)