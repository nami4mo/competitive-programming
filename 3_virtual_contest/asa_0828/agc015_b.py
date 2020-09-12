s = input()
ans = 0
for i, si in enumerate(s):
    kai = i+1
    rem = len(s) - kai
    if si == 'U':
        ans += rem
    else:
        ans += rem*2

for i, si in enumerate(s[::-1]):
    kai = i+1
    rem = len(s) - kai
    if si == 'D':
        ans += rem
    else:
        ans += rem*2

print(ans)