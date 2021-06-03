n,k=map(int, input().split())
ns=str(n)

from itertools import combinations
ll = list(range(10))  # list of elements
combl = list(combinations(ll, k))
for comb in combl:
    # big
    val_l=[]
    val_s=[]
    st=set(comb)
    same=True
    for ni in ns:
        if same:
            if int(ni) in st:
                val_l.append(ni)
                val_s.append(ni)
            else:
                val_s.append()
