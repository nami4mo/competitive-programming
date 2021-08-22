m,k = map(int, input().split())

# if k == 0:


if m==0:
    if k==0:
        print(0,0)
    else:
        print(-1)
    exit()

if m==1:
    if k == 0:
        print(0,0,1,1)
    else:
        print(-1)
    exit()

if k >= 2**m:
    print(-1)
    exit()

ansl = []
for i in range(2**m):
    if i != k: ansl.append(i)
ansl.append(k)
for i in range(2**m-1,-1,-1):
    if i != k: ansl.append(i)
ansl.append(k)

print(*ansl)