from bisect import bisect_left, bisect_right

MAX=10**5+10
n=int(input())
al=list(map(int, input().split()))
amax=max(al)
starts=[-1]*(MAX)
lasts=[-1]*(MAX)
posl=[[] for _ in range(MAX)]
for i,a in enumerate(al):
    if a==amax and i==0:continue
    lasts[a]=i
    if starts[a]==-1:starts[a]=i
    posl[a].append(i)

loop=1
pos=0
for i in range(MAX):
    if starts[i]==-1:continue
    if pos<=starts[i]:
        pos=lasts[i]
    else:
        loop+=1
        # pos=lasts[i]
        ind = bisect_right(posl[i],pos)-1
        pos=posl[i][ind]

print(loop)