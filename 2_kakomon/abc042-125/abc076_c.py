s = str(input())
t = str(input())

ans_ind = -1
for i in range(len(s)-len(t)+1):
    for j in range(0,len(t)):
        if s[i+j] == t[j] or s[i+j] == '?':
            pass
        else:
            break
    else:
        ans_ind = i

if ans_ind == -1:
    print('UNRESTORABLE')
else:
    ans = ''
    for i in range(len(s)):
        if ans_ind <= i < ans_ind + len(t):
            ans += t[i-ans_ind]
        else:
            if s[i] == '?': ans += 'a'
            else: ans += s[i]
    print(ans)