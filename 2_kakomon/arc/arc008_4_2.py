# 検証用にコピペで借りたSegTree
class Segtree:
 
    def __init__(self, n, operator, identity):
        """
        n:データ配列のサイズ
        operator:演算子(モノイド)。関数オブジェクト
        identity:演算子に対応する単位元
        """
        nb = bin(n)[2:]
        bc = sum([int(digit) for digit in nb])
        if bc == 1:
            self.num_end_leaves = 2**(len(nb)-1)
        else:
            self.num_end_leaves = 2**(len(nb))
 
        self. array = [identity for i in range(self.num_end_leaves * 2)]
 
        self.identity = identity
        self.operator = operator
 
    def update(self, x, val):
        """
        x:代入する場所
        val:代入する値
        """
        actual_x = x+self.num_end_leaves
        self.array[actual_x] = val
        while actual_x > 0:
            actual_x //= 2
            self.array[actual_x] = self.operator(self.array[actual_x*2], self.array[actual_x*2+1])
 
    def get(self, q_left, q_right, arr_ind=1, leaf_left=0, depth=0):
        """
        q_left:クエリ区間の左
        q_right:クエリ区間の右
        arr_ind:木配列のインデックス。最初は親なので1
        leaf_left:木配列インデックスに対して、それが表す葉がカバーする範囲の左
        depth:木配列での深さ。カバー範囲の広さの計算に使用
        """
        width_of_floor = self.num_end_leaves//(2**depth)
        leaf_right = leaf_left + width_of_floor - 1
 
        if leaf_left > q_right or leaf_right < q_left:
            return self.identity
 
        elif leaf_left >= q_left and leaf_right <= q_right:
            return self.array[arr_ind]
 
        else:
            val_l = self.get(q_left, q_right, arr_ind*2, leaf_left, depth+1)
            val_r = self.get(q_left, q_right, arr_ind*2+1, leaf_left+width_of_floor//2, depth+1)
            return self.operator(val_l, val_r)

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

def merge(a,b):
    return (a[0]*b[0], b[0]*a[1]+b[1])
vl=[(1,0)]*len(pl)
st = Segtree(len(pl),merge,(1,0))
# print(p2i)
# print(pl)

ansmax=1
ansmin=1
for p,a,b in pabl:
    st.update(p2i[p],(a,b))
    ai,bi=st.get(0,len(pl))
    # print((ai,bi))
    val=ai+bi
    ansmax=max(ansmax,val)
    ansmin=min(ansmin,val)
# print('{:.08f}'.format(ansmin))
# print('{:.08f}'.format(ansmax))
print(ansmin)
print(ansmax)