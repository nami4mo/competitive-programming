t=int(input())
for _ in range(t):
    a,k = map(int, input().split())
    ans = 10**9
    
    if a >= k:
        if (a+k)%2 == 0:
            ans = 0
        else:
            ans = 1

    ans = min(abs(a-k),ans)
    print(ans)