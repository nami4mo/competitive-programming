n=int(input())
# TODO: remove 0,1
al=[2]*(n+1)
for i in range(2,n+1):
    val=al[i]
    for j in range(i+i,n+1,i):
        if al[j]<val+1: al[j]=val+1

al[1]=1
print(*al[1:])