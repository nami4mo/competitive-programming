s = input()
ans = 0
for i,si in enumerate(s):
    if i%2 == 0:
        ans += int(si)
    else:
        ans -= int(si)

print(ans)