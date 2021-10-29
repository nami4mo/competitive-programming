

def main():
    h,w,n=map(int, input().split())
    rcal=[]
    for i in range(n):
        r,c,a=map(int, input().split())
        r-=1
        c-=1
        rcal.append((r,c,a,i))
    rcal.sort(key=lambda x:-x[2])
    rcnts=[-1]*h
    ccnts=[-1]*w
    ans=[-1]*n
    que=[]
    prev_a=-1
    for r,c,a,i in rcal:
        if a!=prev_a:
            for rq,cq,vq in que:
                rcnts[rq]=max(rcnts[rq],vq)
                ccnts[cq]=max(ccnts[cq],vq)
            que.clear()
        rv=rcnts[r]+1
        cv=ccnts[c]+1
        val=max(rv,cv)
        que.append((r,c,val))
        ans[i]=val
        prev_a=a

    for  a in ans:print(a)
        


if __name__ == "__main__":
    main()