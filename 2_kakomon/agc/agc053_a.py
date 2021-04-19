n=int(input())
s=list(input())
al=list(map(int, input().split()))

k=10**10
for i in range(n):
    d=al[i+1]-al[i]
    k=min(k,abs(d))

print(k)
for i in range(k):
    bl=[]
    for j in range(n+1):
        b=(al[j]+i)//k
        bl.append(b)
    print(*bl)