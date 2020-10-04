n = int(input())
s = input()

lc = 0
rc = 0
for i in range(1,n):
    if s[i] == 'E': rc += 1

ans = rc
for i in range(1,n):
    new_s = s[i-1]
    if new_s == 'W': lc += 1
    poped_s = s[i]
    if poped_s == 'E':
        rc -= 1
    ans = min(ans, lc+rc)

print(ans)