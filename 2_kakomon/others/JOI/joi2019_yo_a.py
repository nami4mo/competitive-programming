a,b,c=map(int, input().split())
cnt=0
for i in range(10**6):
    cnt+=a
    if (i+1)%7==0: cnt+=b
    if cnt>=c:
        print(i+1)
        exit()