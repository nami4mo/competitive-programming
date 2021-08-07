def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

def p_factorization_t(n, ps):
    res=[]
    for p in ps:
        if n%p==0:res.append(p)
    return res
    

ps=primes(72)
print(len(ps))
a,b=map(int, input().split())
facs=set()
for i in range(a,b+1):
    f=p_factorization_t(i,ps)
    for p in f:
        facs.add(p)

if b==a:
    print(2)
    exit()

facs=list(facs)
d={}
for i,f in enumerate(facs):
    d[f]=pow(2,i)

plen=(pow(2,len(facs))) 
dp=[[0]*plen for _ in range(b-a+2)]
dp[0][0]=1

for i in range(a,b+1):
    f=p_factorization_t(i,ps)
    vals=0
    for p in f:
        pd=d[p]
        vals+=pd
    for j in range(plen):
        if vals&j==0:
            dp[i+1-a][j+vals]+=dp[i-a][j]

    for j in range(plen):
        dp[i+1-a][j]+=dp[i-a][j]
    
ans=sum(dp[-1])
print(ans)