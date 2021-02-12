s = input()
n = len(s)

l = 0
r = n-1
ans = 0
while True:
    if s[l] == s[r]:
        l += 1
        r -= 1
    else:
        if s[l] == 'x':
            l += 1
            ans += 1
        elif s[r] == 'x':
            r -= 1
            ans += 1
        else:
            print(-1)
            exit()
    if l >= r:
        break

print(ans)