n,a,b = map(int, input().split())
ans1 = min(a,b)
ans2 = a+b-n
ans2 = max(ans2,0)
print(ans1,ans2)