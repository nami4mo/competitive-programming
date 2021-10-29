

def main():
    n,d=map(int, input().split())
    MOD=998244353
    csum=[0]
    for i in range(d+1):
        cnt=pow(2,max(0,i-1),MOD)*pow(2,max(0,d-i-1),MOD)
        cnt%=MOD
        csum.append((csum[-1]+cnt)%MOD)
    ans=0
    # print(csum)
    for i in range(1,n+1):
        dist=n-i
        if dist>=d:
            ans+=csum[-1]*pow(2,i-1,MOD)
            ans%=MOD
        elif dist*2<d:continue
        else:
            dist2=d-dist
            if dist>dist2:dist,dist2=dist2,dist
            val=csum[dist2+1]-csum[dist]
            ans+=val*pow(2,i-1,MOD)
            ans%=MOD
        # print(ans)
    ans*=2
    ans%=MOD
    print(ans)



if __name__ == "__main__":
    main()