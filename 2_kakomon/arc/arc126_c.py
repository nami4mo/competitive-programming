MAX=3*10**5+10
def main():
    n,k=map(int, input().split())
    al=list(map(int, input().split()))
    al.sort()

    need=0
    for a in al:
        need+=(al[-1]-a)
    if need<=k:
        rem=k-need
        up=rem//n
        print(al[-1]+up)
        return

    cnt_csums=[0]*MAX
    cnts=[0]*MAX
    for a in al:
        cnts[a]+=1
    for i in range(1,MAX):
        cnt_csums[i]=cnt_csums[i-1]+cnts[i]
    asum=sum(al)
    
    for target in range(al[-1]-1,0,-1):
        val=0
        for next_v in range(target, MAX+target, target):
            cnt=cnt_csums[min(next_v,MAX-1)]-cnt_csums[next_v-target]
            val+=cnt*next_v
        need=val-asum
        if need<=k:
            print(target)
            return

if __name__ == "__main__":
    main()
