n=int(input())
al=list(map(int, input().split()))
al.sort()
for i in range(n):
    if al[i]!=i+1:
        print('No')
        exit()
print('Yes')