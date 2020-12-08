x,y,a,b,c=map(int, input().split())
al=list(map(int, input().split()))
bl=list(map(int, input().split()))
cl=list(map(int, input().split()))

al.sort(reverse=True)
bl.sort(reverse=True)
cl.sort(reverse=True)

abl = al[:x]+bl[:y]
abl.sort(reverse=True)

abl = abl + cl[:max(c,x+y)]
abl.sort(reverse=True)

print(sum(abl[:x+y]))