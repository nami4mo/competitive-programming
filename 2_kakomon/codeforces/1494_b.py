from itertools import product

for _ in range(int(input())):
    n,u,r,b,l=map(int, input().split())
    ite = list(product(range(2),repeat=4))
    for pattern in ite:
        ok=True
        vl=list(pattern)
        if not vl[0]+vl[1]<=u<=vl[0]+vl[1]+(n-2): ok=False
        if not vl[1]+vl[2]<=r<=vl[1]+vl[2]+(n-2): ok=False
        if not vl[2]+vl[3]<=b<=vl[2]+vl[3]+(n-2): ok=False
        if not vl[3]+vl[0]<=l<=vl[3]+vl[0]+(n-2): ok=False
        if ok:
            print('YES')
            break
    else:
        print('NO')