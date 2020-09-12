n,m = map(int, input().split())
xl = list(map(int, input().split()))
xl.sort()
selected = m-n
if selected <= 0:
    print(0)
    exit()

diffs = []
for x1,x2 in zip(xl[:-1],xl[1:]):
    diff = x2-x1
    diffs.append(diff)

diffs.sort()
ans = sum(diffs[:selected])
print(ans)