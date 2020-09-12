n = int(input())
s = input()
t = input()

ans = 0
for i in range(n):
    curr_s = s[i:]
    cnt = 0
    for j in range(n-i):
        if t[j] == curr_s[j]: cnt += 1
        else: break
    ans = max(ans,cnt)

ans = n*2 - ans
print(ans)