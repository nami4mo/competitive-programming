h = int(input())
w = int(input())
n = int(input())
v = max(h,w)
cnt = (n-1)//v + 1
print(cnt)