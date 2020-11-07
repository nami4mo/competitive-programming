n = int(input())
abl = []
for _ in range(n):
    a,b = map(int, input().split())
    abl.append((a,b))

abl = abl[::-1]
ans = 0
for a,b in abl:
    curr_a = ans+a
    rem = b-(curr_a%b)
    if rem == b: continue
    ans += rem

print(ans)