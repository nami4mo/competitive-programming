x,y=  map(int, input().split())
k = int(input())

if y >= k:
    print(x+k)
else:
    rem = k-y
    x -= rem
    print(x+y)

