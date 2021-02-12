from typing import Deque

from collections import deque

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
                v_r = self.seg_f(v_r, self.tree[r-1])
                r -= 1
            l >>= 1
            r >>= 1
        return self.seg_f(v_l ,v_r)


INF = 10**10
h,w,m=map(int, input().split())
xyl=[]
ytoxl = [[] for _ in range(h)]
# xtoyl = [[] for _ in range(w)]
xmins = [INF]*w
ymins = [INF]*h
for i in range(m):
    y,x=map(int, input().split())
    x-=1
    y-=1
    xmins[x] = min(xmins[x],y)
    ymins[y] = min(ymins[y],x)
    xyl.append((x,y))
    ytoxl[y].append(x)
    # xtoyl[x].append(y)

vl = []
for i in range(w):
    if xmins[i] == INF:
        vl.append(1)
    else:
        vl.append(0)

def add(a,b): return a+b
st = SegTree(vl, add, 0)

ans = 0
y_start = xmins[0]-1
x_end = ymins[0]
x_end = min(w,x_end)
for y in range(h-1,-1,-1):

    if y <= y_start:
        if ymins[y] == INF:
            ans += w
        else:
            ans += st.query(ymins[y]+1,x_end)
            ans += ymins[y]
    else:
        ans += st.query(1,x_end)
        # ans += ymins[y]
    for x in ytoxl[y]:
        if xmins[x] == y:
            st.update(x,1)
    # print('^')
    # print(y,ans)

print(ans)