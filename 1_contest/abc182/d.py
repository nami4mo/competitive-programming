n = int(input())
al = list(map(int, input().split()))

csum = 0
pos = 0
csums = []
curr_max = 0

ans = 0
for i, a in enumerate(al):
    csum += a
    curr_max = max(curr_max, csum)
    ans = max(ans, pos+curr_max)
    pos += csum

print(ans)