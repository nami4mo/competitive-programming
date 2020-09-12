class RollingHash():
    def __init__(self, s, base1=2187,base2=6561):
        self.mod = 2^61-1
        self.s = s
        n = len(s)
        self.hash1 = [0]*(n+1)
        self.pow1 = [1]*(n+1)
        self.hash2 = [0]*(n+1)
        self.pow2 = [1]*(n+1)
        for i in range(n):
            self.hash1[i+1] = (self.hash1[i]*base1 + ord(s[i])) % self.mod
            self.pow1[i+1] = (self.pow1[i]*base1) % self.mod
            self.hash2[i+1] = (self.hash2[i]*base2 + ord(s[i])) % self.mod
            self.pow2[i+1] = (self.pow2[i]*base2) % self.mod

    def get(self, l, r):
        h1 = (self.hash1[r] - self.hash1[l] * self.pow1[r-l]) % self.mod
        h2 = (self.hash2[r] - self.hash2[l] * self.pow2[r-l]) % self.mod
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