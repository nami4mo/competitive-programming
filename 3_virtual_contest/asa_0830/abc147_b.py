s=input()
ans = 0
for i in range(len(s)):
    j = len(s)-i-1
    if i > j: break
    if s[i] != s[j]: ans += 1

print(ans)