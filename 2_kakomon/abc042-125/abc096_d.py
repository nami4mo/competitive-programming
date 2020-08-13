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


n = int(input())
ps = get_sieve_of_eratosthenes(55555)
ansl = []
for p in ps:
    if p%5 == 1:
       ansl.append(p) 

print(*ansl[:n])
