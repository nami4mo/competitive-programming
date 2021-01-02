a,b,c=map(int, input().split())
for i in range(1,100):
    v=a*i
    if v%b==c:
        print('YES')
        break
else:
    print('NO')