n = int(input())
al = list(map(int, input().split()))

ans_v = 0
ans = 2
for k in range(2,1000):
    cnt = 0
    for a in al:
        if a%k == 0: cnt+=1
    if ans_v < cnt:
        ans_v = cnt
        ans = k

print(ans)