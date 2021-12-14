

def main():
    n,m=map(int, input().split())
    abl=[]
    rems=[0]*n
    gl=[[] for _ in range(n)]
    for _ in range(m):
        a,b=map(int, input().split())
        a-=1
        b-=1
        abl.append((a,b))
        rems[a]+=1
        rems[b]+=1
        gl[a].append(b)
        gl[b].append(a)

    for i in range(n):
        if rems[i]>2:
            print('No')
            exit()

    used=[False]*n

    from collections import deque
    for i in range(n):
        if used[i]:continue
        q=deque()
        q.append((i,-1))
        used[i]=True
        while q:
            poped,prev=q.popleft()
            for neib in gl[poped]:
                if neib==prev:continue
                if used[neib]:
                    print('No')
                    exit()
                q.append((neib,poped))
                used[neib]=True

    print('Yes')


    # for i in range(n):
    #     if rems[i]>2:
    #         print('No')
    #         exit()

    
    # for i in range(n):
    #     if rems[i]>2:
    #         print('No')
    #         exit()

    #     if rems[i]==0:
    #         continue

    #     if used[i]:
    #         continue

    #     start=i
    #     for neib in gl[i]:
    #         c=neib
    #         while True:
    #             print(c)

    #             used[c]=True
    #             if rems[c]==1:
    #                 rems[c]-=1
    #                 break
    #             if rems[c]==2:
    #                 rems[c]-=1
    #                 nexts=gl[c]
    #                 c=nexts[0]
    #                 if used[c]:
    #                     c=nexts[1]
    #                 if used[c]:
    #                     print('No')
    #                     return
    # print('Yes')






if __name__ == "__main__":
    main()