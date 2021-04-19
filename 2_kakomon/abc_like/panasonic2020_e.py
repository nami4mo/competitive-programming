def check(s,t):
    ml=min(len(s),len(t))
    res=True
    for i in range(ml):
        if s[i]!=t[i] and s[i]!='?' and t[i]!='?':
            res=False
            break
    return res

MAX=4000
a=list(input())
b=list(input())
c=list(input())
an,bn,cn=len(a),len(b),len(c)
m_ab,m_bc,m_ca=[False]*(MAX*2+1),[False]*(MAX*2+1),[False]*(MAX*2+1)

for i in range(-MAX,MAX+1):
    ind=i+MAX
    if i<=0:
        if -i>=an: 
            m_ab[ind]=True
            m_ca[ind]=True
        else:
            ta=a[-i:]
            res=check(ta,b)
            m_ab[ind]=res
            res=check(ta,c)
            m_ca[ind]=res

        if -i>=cn: 
            m_bc[ind]=True
        else:
            tc=c[-i:]
            res=check(tc,b)
            m_bc[ind]=res

    else:
        if i>=bn:
            m_ab[ind]=True
            m_bc[ind]=True
        else: 
            tb=b[i:]
            res=check(a,tb)
            m_ab[ind]=res
            res=check(c,tb)
            m_bc[ind]=res

        if i>=cn:
            m_ca[ind]=True
        else:
            tc=c[i:]
            res=check(tc,a)
            m_ca[ind]=res

ans=10**10
for i in range(-MAX,MAX+1):
    for j in range(-MAX,MAX+1):
        iind,jind=i+MAX,j+MAX
        if (not m_ab[iind]) or (not m_bc[jind]):continue
        d=i-j+MAX
        if (not 0<=d<MAX*2) or m_ca[d]:
            left=min(0,i,j)
            right=max(len(a)+i, len(b), len(c)+j)
            ans=min(ans, right-left)
print(ans)