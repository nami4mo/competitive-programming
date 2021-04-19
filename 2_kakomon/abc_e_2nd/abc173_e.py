def modinv(a,m):
    b, u, v = m, 1, 0
    while b:
        t = a//b
        a -= t*b
        a,b = b,a
        u -= t * v
        u,v = v,u
    u %= m
    return u

n,k=map(int, input().split())
al=list(map(int, input().split()))
MOD=10**9+7

aal=[]
zero=0
posi=0
nega=0
for a in al:
    if a!=0: aal.append((abs(a),a//abs(a)))
    if a==0:zero+=1
    elif a>0:posi+=1
    else:nega+=1
aal.sort(reverse=True)

# zero
if posi+nega<k:
    print(0)
    exit()

# posi+nega>=k
if posi+nega==k and nega%2==1:
    if zero>0:
        print(0)
        exit()
    #...
    ans=1
    for a,_ in aal[:k]:
        ans*=a
        ans%=MOD
    ans*=(-1)
    ans%=MOD
    print(ans)
    exit()

if posi==0 and k%2==1:
    if zero>0:
        print(0)
        exit()
    aal.sort()
    ans=1
    for a,_ in aal[:k]:
        ans*=a
        ans%=MOD
    ans*=-1
    ans%=MOD
    print(ans)
    exit()

ans=1
nc=0
n_min=10**10
p_min=10**10
for a,sig in aal[:k]:
    if sig==-1:
        nc+=1
        n_min=a
    else:
        p_min=a
    ans*=a
    ans%=MOD
    
if nc%2==0:
    print(ans)
    exit()

pp=0
nn=0
for a,sig in aal[k:]:
    if pp!=0 and nn!=0:break
    if sig==1:
        pp=max(pp,a)
    else:
        nn=max(nn,a)

if pp*p_min-nn*n_min>=0:
    ans*=modinv(n_min,MOD)
    ans*=pp
else:
    ans*=modinv(p_min,MOD)
    ans*=nn
print(ans%MOD)