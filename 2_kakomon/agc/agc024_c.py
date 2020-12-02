import sys
input = sys.stdin.readline
n=int(input())
al=[int(input()) for _ in range(n)]

if al[0]!=0:
    print(-1)
    exit()

ans=0
for i in range(1,n):
    if al[i-1]+1 < al[i]:
        print(-1)
        exit()
    if al[i-1]+1 == al[i]:
        ans+=1
    else:
        ans+=al[i]

print(ans)