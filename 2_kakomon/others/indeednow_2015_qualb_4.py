n,c=map(int, input().split())
al=list(map(int, input().split()))

lasts=[-1]*(c+1)
ansl=[0]*(c+1)
for i,a in enumerate(al):
    lastai=lasts[a]
    dist=i-lastai-1
    ansl[a]+=(dist+1)*dist//2
    lasts[a]=i
    # print(ansl)

for i in range(c+1):
    ansl[i]+=(n-lasts[i])*(n-lasts[i]-1)//2

# print(ansl)
lrsum=(n+1)*n//2
for a in ansl[1:]:
    print(lrsum-a)