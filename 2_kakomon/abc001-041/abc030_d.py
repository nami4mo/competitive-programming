n,a=map(int, input().split())
k=input()
bl=[-1]+list(map(int, input().split()))

visited=[-1]*(n+1)
visited[a]=0
curr=a
loop_l=-1
loop_s=-1
for i in range(n):
    to=bl[curr]
    if visited[to]==-1:
        visited[to]=visited[curr]+1
    else:
        loop_l=visited[curr]-visited[to]+1
        loop_s=to
        break
    curr=to

if len(k)<=6:
    k=int(k)
    loop_sd=visited[loop_s]
    if k<=loop_sd:
        for i in range(n+1):
            if visited[i]==k:
                print(i)
                exit()
    else:
        k-=loop_sd
        k%=loop_l
        curr=loop_s
        for i in range(k):
            to=bl[curr]
            curr=to
        print(curr)
    exit()

rem=0
for ki in k:
    rem=rem*10+int(ki)
    rem%=loop_l

loop_sd=visited[loop_s]
rem-=loop_sd
rem%=loop_l

k=rem
curr=loop_s
for i in range(k):
    to=bl[curr]
    curr=to
print(curr)
