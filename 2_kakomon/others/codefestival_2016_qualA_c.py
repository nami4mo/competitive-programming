s=input()
k=int(input())

ans = []
rem = k
for si in s[:-1]:
    if si == 'a':
        to_a = 0
    else:
        to_a = ord('z') - ord(si) + 1

    if to_a <= rem:
        rem -= to_a
        ans.append('a')
    else:
        ans.append(si)
        # next_s = chr(ord(si) + rem)
        # ans.append(next_s)
        # rem = 0


last_s_ord = (ord(s[-1]) + rem - ord('a'))%26
last_s = chr(ord('a') + last_s_ord)
ans.append(last_s)
ans = ''.join(ans)
print(ans)