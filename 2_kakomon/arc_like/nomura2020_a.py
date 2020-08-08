h1,m1,h2,m2,k = map(int, input().split())

min1 = h1*60+m1
min2 = h2*60+m2

ans = min2-min1-k
ans = max(0,ans)
print(ans)