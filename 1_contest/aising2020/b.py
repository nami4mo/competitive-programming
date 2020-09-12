n = int(input())
al = list(map(int, input().split()))

ans = 0
for i, a in enumerate(al):
    if (i+1)%2 == 1 and a%2 == 1: ans+=1

print(ans)