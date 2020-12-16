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

# s = 'abcdefghijk'
# t = 'cde'
# rhs = RollingHash(s)
# rht = RollingHash(t)

# th = rht.get(0,len(t))
# for i in range(len(s)-len(t)):
#     sh = rhs.get(i,i+len(t))
#     if th == sh:
#         print(i)

n=int(input())
s=input()
tl=[input() for _ in range(n)]
cnts=[[0]*(len(s)+1) for _ in range(len(s))]
rhs=RollingHash(s)

for t in tl:
    rht=RollingHash(t)
    tlen=len(t)
    th=rht.get(0,tlen)
    for i in range(len(s)-len(t)+1):
        sh=rhs.get(i,i+tlen)
        if sh==th:
            cnts[i][i+tlen]+=1

# for c in cnts:
#     print(c)
# dp=[[0]*(len(s)+1) for _ in range(len(s)+1)]
# dp[0][0]=1
MOD=10**9+7
dp=[0]*(len(s)+1)
dp[0]=1
for i in range(len(s)):
    cnts_row = cnts[i]
    for j in range(len(s)+1):
        dp[j]+=dp[i]*cnts_row[j]
        dp[j]%=MOD

print(dp[-1])