n = int(input())
xl = list(map(int, input().split()))

ans = 10**18
for i in range(0,101):
    curr_sum = 0
    for x in xl:
        curr_sum += (i-x)*(i-x)
    ans = min(ans,curr_sum)

print(ans)