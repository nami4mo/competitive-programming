alps = 'abcdefghijklmnopqrstuvwxyz'

n = int(input())
if n == 1:
    print('a')
    exit()

ansl = []
curr_n = n
for i in range(15, -1, -1):
    if n <= pow(26,i):
        continue
    val = curr_n//pow(26,i)
    ansl.append(val)
    curr_n -= val*pow(26,i)


for j in range(100):
    for i in range(len(ansl)-1):
        if ansl[i+1] == 0:
            ansl[i+1] = 26
            ansl[i] -= 1

ans = ''
for a in ansl:
    if a == 0: continue
    ans += alps[a-1]

print(ans)