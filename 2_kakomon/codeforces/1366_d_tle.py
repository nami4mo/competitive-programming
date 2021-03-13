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


ps=primes(int(10**(3.5))+1)
# print(len(ps))
n=int(input())
al=list(map(int, input().split()))
dic={}

dl1=[]
dl2=[]
for a in al:
    if a in dic:
        d1,d2=dic[a]
        dl1.append(d1)
        dl2.append(d2)
        continue
    for p in ps:
        if a%p!=0:continue
        v=a
        d1=1
        while v%p==0:
            d1*=p
            v//=p
        d2=a//d1
        if d2==1:
            d1,d2=-1,-1
        dl1.append(d1)
        dl2.append(d2)
        dic[a]=(d1,d2)
        break
    else:
        dic[a]=(-1,-1)
        dl1.append(-1)
        dl2.append(-1)

print(*dl1)
print(*dl2)