n=int(input())
ngs=[int(input()) for _ in range(3)]
if n in ngs:
    print('NO')
    exit()
for _ in range(100):
    if n<=3:
        print('YES')
        exit()
    for i in range(3,0,-1):
        if n-i not in ngs:
            n-=i
            break
    else:
        print('NO')
        exit()
print('NO')
exit()