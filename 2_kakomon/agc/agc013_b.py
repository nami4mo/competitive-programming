n,m=map(int, input().split())
gl=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int, input().split())
    a-=1
    b-=1
    gl[a].append(b)
    gl[b].append(a)

visited=[False]*(n)
s1=0
s2=gl[s1][0]
visited[s1]=True
visited[s2]=True

fronts=[]
curr=s1
while True:
    for neib in gl[curr]:
        if not visited[neib]:
            fronts.append(neib)
            visited[neib]=True
            curr=neib
            break
    else:
        break

backs=[]
curr=s2
while True:
    for neib in gl[curr]:
        if not visited[neib]:
            backs.append(neib)
            visited[neib]=True
            curr=neib
            break
    else:
        break

ansl=fronts[::-1]+[s1,s2]+backs
ansl=[a+1 for a in ansl]
print(len(ansl))
print(*ansl)