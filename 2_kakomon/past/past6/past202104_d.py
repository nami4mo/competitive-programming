n,k=map(int, input().split())
al=list(map(int, input().split()))
csum=sum(al[:k])
print(csum)
for i in range(n-k):
    csum-=al[i]
    csum+=al[i+k]
    print(csum)
