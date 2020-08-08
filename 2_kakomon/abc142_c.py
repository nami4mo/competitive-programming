n = int(input())

al = list(map(int, input().split()))
ail = []
for i,a in enumerate(al):
    ail.append((a,i+1))

ail.sort()
ans = []
for a,i in ail:
    ans.append(i)

print(*ans)