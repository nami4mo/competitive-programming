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

n=int(input())
if n==1:
    print('Not Prime')
    exit()

ps=primes(int(n**0.5)+10)
for p in ps:
    if n==p:
        print('Prime')
        exit()
    if n%p==0:
        break
else:
    print('Prime')
    exit()

s=0
for ni in str(n): s+=int(ni)
if n%2!=0 and n%5!=0 and s%3!=0:
    print('Prime')
    exit()


print('Not Prime')