n,k,a=map(int, input().split())
for _ in range(k-1):
    a+=1
    if a>n:a=1
print(a)