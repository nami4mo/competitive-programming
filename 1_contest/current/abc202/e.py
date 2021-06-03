import sys
input = sys.stdin.readline

class Bit:
    """ used for only int(>=0) 
        0-indexed 
    """
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
        self.depth = n.bit_length()
 
    def _sum(self, i):
        i+=1
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def sum(self,l,r):
        return self._sum(r-1)-self._sum(l-1)
 
    def add(self, i, x):
        i+=1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def lower_bound(self, x):
        """ 累積和がx以上になる最小のindexと、その直前までの累積和 """
        sum_ = 0
        pos = 0
        for i in range(self.depth, -1, -1):
            k = pos + (1 << i)
            if k <= self.size and sum_ + self.tree[k] < x:
                sum_ += self.tree[k]
                pos += 1 << i
        return pos, sum_

    def get_less_than_x_cnt(self, x):
        """ 累積和がx未満 の個数 """
        lb_pos, lb_sum = self.lower_bound(x)
        return lb_pos-1

    def get_less_than_and_x_cnt(self, x):
        """ 累積和がx以下 の個数 """
        lb_pos, lb_sum = self.lower_bound(x+1)
        return lb_pos-1
    
    def get_more_than_x_cnt(self, x):
        """ 累積和がxより大きい 個数 """
        return self.size - self.get_less_than_and_x_cnt(x)

# https://qiita.com/Kiri8128/items/2b0023bed9af642c751c
def EulerTour(n, X, i0):
    done = [0] * n
    Q = [~i0, i0] # 根をスタックに追加
    ET = []
    while Q:
        i = Q.pop()
        if i >= 0: # 行きがけの処理
            done[i] = 1
            ET.append(i)
            for a in X[i][::-1]:
                if done[a]: continue
                Q.append(~a) # 帰りがけの処理をスタックに追加
                Q.append(a) # 行きがけの処理をスタックに追加

        else: # 帰りがけの処理
            ET.append(~i)
    return ET


from collections import deque

n=int(input())
pl=list(map(int, input().split()))
gl=[[] for _ in range(n)]
for i,p in enumerate(pl):
    gl[i+1].append(p-1)
    gl[p-1].append(i+1)

et=EulerTour(n,gl,0)
pstart=[-1]*n
pend=[-1]*n
for i, e in enumerate(et):
    if pstart[e]==-1:pstart[e]=i
    else:pend[e]=i


dists=[-1]*(n)
dists[0]=0
q=deque([0])
dmax=0
while q:
    poped=q.popleft()
    d=dists[poped]
    for neib in gl[poped]:
        if dists[neib]!=-1:continue
        dists[neib]=d+1
        q.append(neib)
        dmax=d+1

vals=[]
ds=[[] for _ in range(n+1)]
for i,e in enumerate(et):
    vals.append(dists[e])
    ds[dists[e]].append(i)

# print(et)
# print(vals)

qn=int(input())
ql=[[] for _ in range(n+1)]
for i in range(qn):
    u,d=map(int, input().split())
    u-=1
    ql[d].append((u,i))

bit=Bit(2*n)
ansl=[-1]*qn
for d in range(n+1):
    for pos in ds[d]:
        bit.add(pos,1)
    for u,i in ql[d]:
        ps=pstart[u]
        pe=pend[u]
        ans=bit.sum(ps,pe+1)
        ansl[i]=ans//2
    for pos in ds[d]:
        bit.add(pos,-1)

for a in ansl:print(a)

# sq=int(len(vals)**0.5)+1
# cntsq=[]

# for i in range(sq):
#     cnts=[0]*(dmax+1)
#     st=sq*i
#     end=min(sq*(i+1),len(vals))
#     for j in range(st,end):
#         cnts[vals[j]]+=1
#     cntsq.append(cnts)


# q=int(input())
# al=[]
# for _ in range(q):
#     u,d=map(int, input().split())
#     if d>dmax:
#         al.append(0)
#         continue
#     u-=1
#     us,ue=pstart[u],pend[u]

#     if ue-us<=sq:
#         ans=0
#         for i in range(us,ue+1):
#             if vals[i]==d:ans+=1
#         al.append(ans//2)
#         continue

#     usq=(us-1)//sq+1
#     ueq=min((ue+1)//sq-1, sq-1)
#     ans=0
#     for i in range(usq,ueq+1):
#         ans+=cntsq[i][d]
    
#     for i in range(us,min(usq*sq,n*2,ue+1)):
#         if vals[i]==d:ans+=1
    
#     for i in range( (ueq+1)*sq, min(n*2,ue+1)):
#         if vals[i]==d:ans+=1
#     al.append(ans//2)

# for a in al:print(a)