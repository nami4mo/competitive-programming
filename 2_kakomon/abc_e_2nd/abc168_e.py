from math import gcd
def frac(a,b):
    g=gcd(a,b)
    a//=g
    b//=g
    if b<0:
        a*=-1
        b*=-1
    return (a,b)

cnts={}
azero=0
bzero=0
abzero=0

n=int(input())
for _ in range(n):
    a,b=map(int, input().split())
    if a==0 and b==0: abzero+=1
    elif a==0: azero+=1
    elif b==0: bzero+=1
    else:
        f=frac(a,b)
        cnts.setdefault(f,0)
        cnts[f]+=1

st=set()
ans=1
MOD=10**9+7
for key,cnt in cnts.items():
    if key in st:continue
    st.add(key)
    cnt2=0
    a,b=key
    a,b=b,a*(-1)
    if b<0: a,b=a*(-1),b*(-1)
    if (a,b) in cnts:
        cnt2=cnts[(a,b)]
        st.add((a,b))
    v=pow(2,cnt,MOD)+pow(2,cnt2,MOD)-1
    ans*=v

ans=ans*(pow(2,azero,MOD)+pow(2,bzero,MOD)-1)
ans+=abzero


ans-=1
print(ans%MOD)