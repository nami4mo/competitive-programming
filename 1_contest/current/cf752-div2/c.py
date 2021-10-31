for _ in range(int(input())):
    n=int(input())
    al=list(map(int, input().split()))
    for i,a in enumerate(al):
        d=i+2
        for di in range(d,1,-1):
            if a%di!=0:break
        else:
            print('NO')
            break
    else:
        print('YES')