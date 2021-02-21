def make_k(joi,res,n,k,s):
    l=0
    r=0
    cnt=0
    if s[0]==joi:cnt+=1
    while True:
        # if joi=='J':print(l,r,cnt)
        if cnt<k:
            r+=1
            if r==n:break
            if s[r]==joi:cnt+=1
        else:
            res[l]=r
            if s[l]==joi:cnt-=1
            l+=1
            if l==n:break


from collections import deque,Counter

n,k=map(int, input().split())
s=input()
c=Counter(s)
if c['J']<k or c['O']<k or c['I']<k:
    print(-1)
    exit()

q=deque(s)
while q[0]!='J':q.popleft()
while q and q[-1]!='I': q.pop()
s=list(q)
n=len(s)
if n<3:
    print(-1)
    exit()

jk=[-1]*n
ok=[-1]*n
ik=[-1]*n

make_k('J',jk,n,k,s)
make_k('O',ok,n,k,s)
make_k('I',ik,n,k,s)

# print(s)
# print(jk)
# print(ok)
# print(ik)

ans=10**10
for left in range(n):
    pos=jk[left]
    if pos==-1:break
    pos=ok[pos]
    if pos==-1:break
    pos=ik[pos]
    if pos==-1:break
    d=pos-left+1
    v=d-k*3
    ans=min(v,ans)

if ans==10**10:ans=-1
print(ans)