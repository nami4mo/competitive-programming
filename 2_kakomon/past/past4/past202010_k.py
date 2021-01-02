class Bit:
    """ used for only int(>=0) 
        1-indexed (ignore 0-index)
    """
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
        self.depth = n.bit_length()
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i


k = int(input())
al_l = []
al_cnts = [] 
al_cnts_sum = [] 
al_tento = [] 
for _ in range(k):
    n = int(input())
    row = list(map(int, input().split()))
    al_l.append(row)

    cnts = [0]*21
    for a in row:
        cnts[a] += 1
    al_cnts.append(cnts)
    csum = []
    c = 0
    for cnt in cnts:
        c += cnt
        csum.append(c)
    al_cnts_sum.append(csum)
    
    
    bit = Bit(20)
    tento = 0
    for i,p in enumerate(row):
        bit.add(p,1)
        tento += (i+1-bit.sum(p))
    al_tento.append(tento)


num_cnts = [0]*21
q = int(input())
bl = list(map(int, input().split()))
MOD = 10**9
ans = 0
for b_ in bl:
    b = b_-1
    ans += al_tento[b]
    for num in range(1,21):
        ans += num_cnts[num]*al_cnts_sum[b][num-1]
    for num in range(1,21):
        num_cnts[num] += al_cnts[b][num]
    ans%=MOD

print(ans)