n, m = map(int, input().split())

right = 2*m+1

if m%2 == 0:
    for i in range(m//2):
        print(1+i, 1+m-i)
        print(2+m+i, right-i)

else:
    center = m+1
    for i in range(m//2):
        print(1+i, center-i)
        print(center+1+i, right-i)
    print(m//2+1, m//2+2)
