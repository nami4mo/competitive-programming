n = int(input())
tl = list(map(int, input().split()))
al = list(map(int, input().split()))

if tl[-1] != al[0]:
    print(0)
    exit()

ans = 1
for i in range(1,n-1):
    if tl[i] > tl[i-1] or al[i] > al[i+1]:
        ans *= 1
    else:
        ans *= min(tl[i],al[i])

    if tl[i] > tl[i-1] and tl[i] > al[i]:
        print(0)
        exit()
    elif al[i] > al[i+1] and al[i] > tl[i]:
        print(0)
        exit()
    ans%=(10**9+7)

print(ans)