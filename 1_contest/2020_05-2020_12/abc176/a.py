n,x,t = map(int, input().split())

cnt = (n-1)//x + 1
ans = cnt*t
print(ans)