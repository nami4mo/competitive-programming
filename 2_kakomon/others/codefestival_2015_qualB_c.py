n,m=map(int, input().split())
al=list(map(int, input().split()))
bl=list(map(int, input().split()))
al.sort()
bl.sort()
if n<m:
    print('NO')
    exit()

ni=0
for i in range(m):
    if ni==n:
        print('NO')
        exit()
    while al[ni]<bl[i]:
        ni+=1
        if ni==n:
            print('NO')
            exit()
    ni+=1
print('YES')