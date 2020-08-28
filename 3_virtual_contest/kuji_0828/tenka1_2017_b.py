n = int(input())
abl = [tuple(map(int, input().split())) for _ in range(n)]
abl.sort()

a_max = abl[-1][0]
b_min = abl[-1][1]
ans = a_max + b_min
print(ans)