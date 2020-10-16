n = int(input())
hl = list(map(int, input().split()))

ans = 0
flag = False
for _ in range(max(hl)):
    flag = False
    for i in range(n):
        if hl[i] > 0:
            hl[i]-=1
            if not flag:
                flag = True
                ans += 1
        else:
            flag = False

print(ans)