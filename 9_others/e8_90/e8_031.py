val=50
for i in range(51):val+=i

MAX=1326
gr=[[-1]*MAX for _ in range(51)]
def rec(w,b):
    if w==0 and b<=1:return 0
    if gr[w][b]!=-1:return gr[w][b]
    st=set()
    if b+w<MAX and w>0: st.add(rec(w-1,b+w))
    for i in range(1,b//2+1):
        st.add(rec(w,b-i))
    for i in range(MAX):
        if i not in st:
            gr[w][b]=i
            return i

n=int(input())
al=list(map(int, input().split()))
bl=list(map(int, input().split()))
xor=0
for a,b in zip(al,bl):
    xor=xor^rec(a,b)
if xor==0:
    print('Second')
else:
    print('First')