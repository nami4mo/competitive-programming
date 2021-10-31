n=int(input())
cnts=[0]*n
for _ in range(n-1):
    a,b=map(int, input().split())
    a-=1
    b-=1
    cnts[a]+=1
    cnts[b]+=1
for i in range(n):
    if cnts[i]==n-1:
        print('Yes')
        exit()
print('No')