k = int(input())
rem = 7%k
alreadys = [False]*k
alreadys[rem] = True

ans = 1
while True:
    if rem == 0:
        print(ans)
        exit()
    ans += 1
    rem = (rem*10+7)%k
    if alreadys[rem]:
        print(-1)
        exit()
    alreadys[rem] = True