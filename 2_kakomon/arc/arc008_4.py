# 0-indexed
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
                # v_r = self.seg_f(v_r, self.tree[r-1])
                v_r = self.seg_f(self.tree[r-1], v_r)
                r -= 1
            l >>= 1
            r >>= 1
        return self.seg_f(v_l ,v_r)


def merge(a,b):
    return (a[0]*b[0], b[0]*a[1]+b[1])

n,m=map(int, input().split())
pl=set()
pabl=[]
for i in range(m):
    p,a,b=map(str, input().split())
    p=int(p)
    a,b=float(a),float(b)
    p-=1
    pl.add(p)
    pabl.append((p,a,b))

pl=list(pl)
pl.sort()
p2i={}
for i,p in enumerate(pl):
    p2i[p]=i

vl=[(1.0,0.0) for _ in range(len(pl))]
st = SegTree(vl,merge,(1.0,0.0))
# print(p2i)
# print(pl)

ansmax=1
ansmin=1
for p,a,b in pabl:
    st.update(p2i[p],(a,b))
    ai,bi=st.query(0,len(pl))
    # print((ai,bi))
    val=ai+bi
    ansmax=max(ansmax,val)
    ansmin=min(ansmin,val)
# print('{:.08f}'.format(ansmin))
# print('{:.08f}'.format(ansmax))
print(ansmin)
print(ansmax)