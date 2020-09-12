n,m,d = map(int, input().split())

if d != 0:
    top = 2*(n-d)*(m-1)
else:
    top = n*(m-1)
bottom = pow(n,2)

print(top/bottom)