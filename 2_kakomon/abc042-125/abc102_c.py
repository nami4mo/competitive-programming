n = int(input())
al =  list(map(int, input().split()))

new_al = []
for i,a in enumerate(al):
    new_al.append(a-i-1)

new_al.sort()
if n%2 == 0:
    med = (new_al[n//2] + new_al[n//2-1])/2
else:
    med = new_al[n//2]

ans = 0
for a in new_al:
    ans += abs(a-med)

print(int(ans))