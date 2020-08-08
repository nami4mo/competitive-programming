def get_sieve_of_eratosthenes(n):
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    prime = [2]
    limit = int(n**0.5)
    data = [i + 1 for i in range(2, n, 2)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]


q = int(input())
lrl = []
for _ in range(q):
    lrl.append(list(map(int, input().split())) )

primes = set(get_sieve_of_eratosthenes(10**5))
like2017s = []
cnt_dict = {}
cnt_dict[-1] = 0
for i in range(10**5//2):
    num = i*2+1
    num2 = (num+1)//2
    if num in primes and num2 in primes:
        cnt_dict[num] = cnt_dict[num-2]+1
    else:
        cnt_dict[num] = cnt_dict[num-2]

for lr in lrl:
    l,r = lr
    print(cnt_dict[r]-cnt_dict[l-2])