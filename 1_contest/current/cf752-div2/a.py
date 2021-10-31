for _ in range(int(input())):
    n=int(input())
    al=list(map(int, input().split()))
    ans=0
    ind=1
    for i,a in enumerate(al):
        if a<=ind:
            ind+=1
        else:
            d=a-ind
            ans+=d
            ind=a+1
    print(ans)