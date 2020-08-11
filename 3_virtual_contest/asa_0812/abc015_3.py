from itertools import product

n,k = map(int, input().split())
tl = []
for _ in range(n):
    row = list(map(int, input().split()))
    tl.append(row)


ite = list(product(range(k),repeat=n))
for pattern in ite:
    val = 0
    for i, v in enumerate(pattern):
        curr_t = tl[i][v]
        val = val^curr_t
    if val == 0: 
        print('Found')
        break
else:
    print('Nothing')