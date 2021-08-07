a,b,c=map(int, input().split())
while True:
    if a<=b*c:break
    a-=1
print(a/b)