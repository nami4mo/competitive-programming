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
                # v_r = self.seg_f(v_r, self.tree[r-1]) ## seg_f(a,b) != seg_f(b,a)
                v_r = self.seg_f(self.tree[r-1], v_r)
                r -= 1
            l >>= 1
            r >>= 1
        return self.seg_f(v_l ,v_r)


w,n=map(int, input().split())
vl = [-1]*(w+1)
vl[0]=0
st = SegTree(vl,max,-1)

for _ in range(n):
    l,r,v=map(int, input().split())
    new_wl=[-1]*(w+1)
    for j in range(w+1):
        left=max(0,j-r)
        right=j-l
        if right<0:continue
        mv=st.query(left,right+1)
        if mv==-1:continue
        new_wl[j]=mv+v
    for j in range(w+1):
        if new_wl[j]==-1:continue
        if st.query(j,j+1)<new_wl[j]:
            st.update(j,new_wl[j])

ans=st.query(w,w+1)
if ans==0:ans=-1
print(ans)