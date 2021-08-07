ansl=[]
for _ in range(int(input())):
    l,r=map(int, input().split())
    if l*2>r:
        ansl.append(0)
        continue
    minl=l*2
    cnt=r-minl+1
    ans=cnt*(cnt+1)//2
    ansl.append(ans)

for a in ansl:print(a)