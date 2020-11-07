a,b,c = map(int, input().split())
ans = 0
for i in range(0,10**6):
    if a%2 == 1 or b%2 == 1 or c%2 == 1:
        print(i)
        exit()
    na = (b+c)//2
    nb = (c+a)//2
    nc = (a+b)//2
    a = na
    b = nb
    c = nc

print(-1)