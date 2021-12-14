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



def main():
    n=int(input())
    al=list(map(int, input().split()))
    bl=list(map(int, input().split()))
    abl=[]
    aset=set()
    dic={}
    for i in range(n):
        a,b=al[i],bl[i]
        abl.append((a,b))
        dic.setdefault((a,b),0)
        dic[(a,b)]+=1
        aset.add(a)
    abl.sort(key= lambda x:(x[1],-x[0]))

    al=list(aset)
    al.sort()
    a2i={}
    i2a=[]
    for i, a in enumerate(al):
        a2i[a]=i
        i2a.append(a)

    # print(abl)

    bit=Bit(n)
    ans=0
    for a,b in abl:
        aa=a2i[a]
        ans+=bit.sum(aa,n)
        bit.add(aa,1)

    ans+=n

    for k,v in dic.items():
        ans+=v*(v-1)//2
    print(ans)
    

    


if __name__ == "__main__":
    main()