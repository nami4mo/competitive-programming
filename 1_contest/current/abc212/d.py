from heapq import heappush, heappop

csum=0
hq=[]
for _ in range(int(input())):
    ql=list(map(int, input().split()))
    if ql[0]==1:
        heappush(hq,ql[1]-csum)
    elif ql[0]==2:
        csum+=ql[1]
    else:
        pop=heappop(hq)
        print(pop+csum)

