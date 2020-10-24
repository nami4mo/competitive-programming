atoi_d = {chr(ord('A') + i): i for i in range(26)}
itoa_d = {i: chr(ord('A') + i%26) for i in range(52)}

n = int(input())
s = input()
ans = ''
for si in s:
    i = atoi_d[si]
    ip = i+n
    ans += itoa_d[ip]

print(ans)