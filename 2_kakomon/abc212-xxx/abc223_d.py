
from heapq import heappop, heappush
def main():
    n,m=map(int, input().split())
    gl=[[] for _ in range(n)]
    degs=[0]*n
    for _ in range(m):
        a,b=map(int, input().split())
        a-=1
        b-=1
        gl[a].append(b)
        degs[b]+=1
    q=[]
    for i in range(n):
        if degs[i]==0:
            heappush(q,i)

    ans=[]
    while q:
        poped=heappop(q)
        ans.append(poped+1)
        for neib in gl[poped]:
            degs[neib]-=1
            if degs[neib]==0:heappush(q,neib)
    if len(ans)==n:
        print(*ans)
    else:print(-1)


if __name__ == "__main__":
    main()