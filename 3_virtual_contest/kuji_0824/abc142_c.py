n = int(input())
al = list(map(int, input().split()))
ail = []
for i,a in enumerate(al):
    ail.append((a,i+1))

ail.sort()
ans = []
for i,a in ail:
    ans.append(a)

print(*ans)