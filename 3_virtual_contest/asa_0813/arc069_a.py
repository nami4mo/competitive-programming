n,m = map(int, input().split())

if n*2 < m:
    c = n*2 + m
    print(c//4)
else:
    print(m//2)