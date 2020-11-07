# n = int(input())
s = input()

ans = 0
for i in range(len(s)):
    left = int(s[:i]) if i != 0 else 0
    right = int(s[i+1:]) if i != len(s)-1 else 0
    r_keta = len(s)-1-i
    if int(s[i]) >= 2:
        ans += (left+1)*(10**r_keta)
    elif int(s[i]) == 1:
        ans += (left)*(10**r_keta)
        ans += (right+1)
    else:
        ans += (left)*(10**r_keta)

print(ans)