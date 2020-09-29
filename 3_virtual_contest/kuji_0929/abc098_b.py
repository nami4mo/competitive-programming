n = int(input())
s = input()

alps = 'abcdefghijklmnopqrstuvwxyz'
ans = 0
for i in range(1,n):
    s1 = s[:i]
    s2 = s[i:]
    cnt = 0
    for alp in alps:
        if alp in s1 and alp in s2:
            cnt += 1
    ans = max(ans,cnt)

print(ans)