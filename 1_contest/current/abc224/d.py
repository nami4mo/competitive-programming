


def main():
    m=int(input())
    d={}
    gl=[[] for _ in range(9)]
    for _ in range(m):
        u,v=map(int, input().split())
        u-=1
        v-=1
        gl[u].append(v)
        gl[v].append(u)
    pl=list(map(int, input().split()))
    pl=[p-1 for p in pl]
    
    from collections import deque
    vals=['8']*9
    for i in range(8):
        vals[pl[i]]=str(i)
    q=deque()
    # print(vals)
    vals=''.join(vals)
    vis={vals:0}
    q.append(vals)
    goal='012345678'
    if vals==goal:
        print(0)
        return
    while q:
        poped=q.popleft()
        popedl=list(poped)
        zero=-1
        for i in range(9):
            if popedl[i]=='8':
                zero=i
                break
        poped=str(poped)
        dist=vis[poped]
        for neib in gl[zero]:
            v2=popedl[:]
            v2[neib],v2[zero]=v2[zero],v2[neib]
            s2=''.join(v2)
            if s2 in vis:continue
            vis[s2]=dist+1
            if s2==goal:
                print(vis[s2])
                return
            q.append(s2)

    print(-1)


if __name__ == "__main__":
    main()