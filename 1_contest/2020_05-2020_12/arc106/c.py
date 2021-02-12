n,m = map(int, input().split())
if n == 1:
    if m == 0:
        print(1,2)
        exit()
    else:
        print(-1)
        exit()
if n == 2:
    if m == 0:
        print(1,2)
        print(3,4)
        exit()
    else:
        print(-1)
        exit()

if m < 0:
    print(-1)
    exit()
if m >= n-1:
    print(-1)
    exit()
if m == 0:
    for i in range(n):
        print(1+i*2,2+i*2)
    exit()    

r = m*2+4
print(1,r)
cnt = m+1
for i in range(cnt):
    ind = i+1
    print(2*ind,2*ind+1)


rem = n-cnt-1
for i in range(rem):
    print(r+1+i*2,r+2+i*2)


