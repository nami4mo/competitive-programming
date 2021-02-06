import sys
sys.setrecursionlimit(10**6)
class RollingHash():
    def __init__(self, s, base1=1007, base2=2009, mod1=10**9+7, mod2=10**9+9):
        self.mod1 = mod1
        self.mod2 = mod2
        self.s = s
        n = len(s)
        self.hash1 = [0]*(n+1)
        self.pow1 = [1]*(n+1)
        self.hash2 = [0]*(n+1)
        self.pow2 = [1]*(n+1)
        for i in range(n):
            self.hash1[i+1] = (self.hash1[i]*base1 + ord(s[i])) % self.mod1
            self.pow1[i+1] = (self.pow1[i]*base1) % self.mod1
            self.hash2[i+1] = (self.hash2[i]*base2 + ord(s[i])) % self.mod2
            self.pow2[i+1] = (self.pow2[i]*base2) % self.mod2

    def get(self, l, r):
        h1 = (self.hash1[r] - self.hash1[l] * self.pow1[r-l]) % self.mod1
        h2 = (self.hash2[r] - self.hash2[l] * self.pow2[r-l]) % self.mod2
        return (h1,h2)




def dfs(node,connect,dp,st,sn,tn):
    if not connect[node]:
        dp[node]=0
        return 0
    if node in st:
        print(-1)
        exit()
    st.add(node)
    dist=dfs((node+tn)%sn,connect,dp,st,sn,tn)+1
    st.remove(node)
    dp[node]=dist
    return dist

s=input()
t=input()
sn=len(s)
tn=len(t)

if sn<=tn:
    mul=(tn-1)//sn+1
    ss=s*mul
    ss*=2
else:
    ss=s*2

rhs = RollingHash(ss)
rht = RollingHash(t)
connect=[False]*(sn)
for i in range(sn):
    if rhs.get(i,i+tn)==rht.get(0,tn):
        connect[i]=True

# print(connect)
dp=[-1]*(sn)
ans=0
for i in range(sn):
    if dp[i]!=-1:continue
    st=set()
    ans=max(ans,dfs(i,connect,dp,st,sn,tn))
print(ans)