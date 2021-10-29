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


def main():
    n,m=map(int, input().split())
    gl=[[] for _ in range(n)]
    for _ in range(m):
        a,b=map(int, input().split())
        a-=1
        b-=1
        gl[a].append(b)
    for i in range(n):
        gl[i].sort(reverse=True)

    vl=[0]*n
    seg=SegTree(vl,max,0)
    for a in range(n):
        for b in gl[a]:
            ma=seg.query(0,b)
            val=seg.query(b,b+1)
            if ma+1>val:seg.update(b,ma+1)
    ans=seg.query(0,n)
    print(ans)



if __name__ == "__main__":
    main()
