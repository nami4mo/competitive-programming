from collections import deque

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


n = int(input())
s = input()
rh = RollingHash(s)

for len_ in range(n//2,0,-1):
    ql = [(-1,-1)]*(len_-1)
    wait_q = deque(ql)
    hset = set()
    # print(len_)
    for i in range(n-len_+1):
        # print(s[i:i+len_])
        hs = rh.get(i,i+len_)
        if hs in hset:
            print(len_)
            exit()
        else:
            wait_q.append(hs)
            hset.add(wait_q.popleft())
        # print(wait_q)
        # print(hset)

else:
    print(0)