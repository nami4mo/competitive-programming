a,b = map(int, input().split())
f = 2*a+100
ans = f-b
if ans <= 0: print(0)
else: print(ans)