
class SegTree:
    def __init__(self, vals, seg_f, ide_ele):
        n = len(vals)
        self.seg_f = seg_f
        self.ide_ele = ide_ele
        self.leaf_n = 1 << (n-1).bit_length()
        self.tree = [ide_ele]*(2*self.leaf_n-1)
        for i in range(n):  # init leaf
            self.tree[i+self.leaf_n-1] = vals[i]
        for i in range(self.leaf_n-2, -1, -1):  # bottom-up
            self.tree[i] = self.seg_f(self.tree[2*i+1], self.tree[2*i+2])

    def update(self, i, x):
        i += (self.leaf_n-1)
        self.tree[i] = x
        while i > 0:
            i = (i-1)//2
            self.tree[i] = self.seg_f(self.tree[2*i+1], self.tree[2*i+2])

    # [l,r)
    def query(self, l, r):
        v_l = self.ide_ele
        v_r = self.ide_ele
        l += (self.leaf_n-1)
        r += (self.leaf_n-1)
        while l < r:
            if l&1 == 0:
                v_l = self.seg_f(v_l, self.tree[l])
            if r&1 == 0:
                v_r = self.seg_f(v_r, self.tree[r-1])
                r -= 1
            l >>= 1
            r >>= 1
        return self.seg_f(v_l ,v_r)


n=int(input())
s=list(input())
q=int(input())
alp_d = {chr(ord('a') + i):SegTree([0]*n,(lambda a,b: a+b),0)  for i in range(26)}
for i in range(n):
    alp_d[s[i]].update(i,1)

ansl = []
for _ in range(q):
    com,a,b = map(str, input().split())
    if com=='1':
        i = int(a)-1
        c = str(b)
        prev_c = s[i]
        alp_d[prev_c].update(i,0)
        alp_d[c].update(i,1)
        s[i] = c
    else:
        l=int(a)-1
        r=int(b)-1
        ans = 0
        for k,v in alp_d.items():
            cnt = v.query(l,r+1)
            if cnt > 0: ans+=1
        ansl.append(ans)

for a in ansl:print(a)