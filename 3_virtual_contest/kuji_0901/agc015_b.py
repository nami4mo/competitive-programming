s = input()
n = len(s)
ans = 0

for i,si in enumerate(s):
    if si == 'U': 
        ans += (n-1) - i
    else:
        ans += 2*(n-1-i)
    

s = s[::-1]
for i,si in enumerate(s):
    if si == 'D': 
        ans += (n-1) - i
    else:
        ans += 2*(n-1-i)

print(ans)