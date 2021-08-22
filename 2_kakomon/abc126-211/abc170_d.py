n = int(input())
a = [-1] + list(map(int, input().split())) + [10**7]
a.sort()

# print(a)
ans = 0
furui = [True]*(10**6+1)
for i in range(1,n+1):
    if not furui[a[i]]: continue
    if a[i-1] != a[i] and a[i] != a[i+1]:
        ans += 1
    for j in range(a[i],10**6+1,a[i]):
        furui[j] = False

print(ans)