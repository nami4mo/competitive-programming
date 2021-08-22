s,k=map(str, input().split())
k=int(k)
n=len(s)
## [(1,2,3),(1,2,4),(1,2,5),(1,3,2),...,(5,4,3)]
from itertools import permutations
ll = list(s)
perml = list(permutations(ll, n))
st=set()
for perm in perml:
    l=list(perm)
    ss=''.join(l)
    st.add(ss)

# print(st)
st=list(st)
st.sort()
print(st[k-1])