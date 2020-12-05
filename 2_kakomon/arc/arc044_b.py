# class Combination:
#     def __init__(self, n_max=10**6, mod=10**9+7):
#         # self._n_max = n_max
#         self._fac, self._finv, self._inv = [0]*n_max, [0]*n_max, [0]*n_max
#         self._fac[0], self._fac[1] = 1, 1
#         self._finv[0], self._finv[1] = 1, 1
#         self._inv[1] = 1
#         self._mod = mod
#         for i in range(2, n_max):
#             self._fac[i] = self._fac[i - 1] * i % self._mod
#             self._inv[i] = self._mod - self._inv[self._mod%i] * (self._mod // i) % self._mod
#             self._finv[i] = self._finv[i - 1] * self._inv[i] % self._mod
#     def com(self, n, r):
#         if n < r: return 0
#         if n < 0 or r < 0: return 0
#         return self._fac[n] * (self._finv[r] * self._finv[n - r] % self._mod) % self._mod

#     def perm(self,n,r):
#         if n < r: return 0
#         if n < 0 or r < 0: return 0
#         return self._fac[n] * (self._finv[n-r] % self._mod) % self._mod

MOD = 10**9+7
# comb = Combination(10**6, MOD)
# # comb.com(10,3)

n=int(input())
al=list(map(int, input().split()))
if al[0]!=0:
    print(0)
    exit()

al.sort()
cntl = []
prev = al[0]
cnt = 1
for a in al[1:]:
    if prev == a: cnt+=1
    else:
        cntl.append((prev,cnt))
        cnt = 1
        prev = a
cntl.append((prev,cnt))

if cntl[0][1] != 1:
    print(0)
    exit()

ans = 1
for i in range(len(cntl)-1):
    p_num,p_cnt = cntl[i]
    num,cnt = cntl[i+1]
    if p_num+1 != num:
        print(0)
        exit()
    from_prev = pow(2,p_cnt,MOD)-1
    all_from_prev = pow(from_prev, cnt, MOD)
    comb = cnt*(cnt-1)//2
    all_comb = pow(2,comb,MOD)
    ans *= all_from_prev
    ans *= all_comb
    ans %=MOD

print(ans)