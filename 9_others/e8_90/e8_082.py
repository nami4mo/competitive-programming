MOD=10**9+7
def cnt(n):
    res=0
    for keta in range(1,20):
        if n>=pow(10,keta):
            num=pow(10,keta)-pow(10,keta-1)
            a0=pow(10,keta-1)
            an=pow(10,keta)-1
            csum=keta*num*(a0+an)//2
            res+=csum
        else:
            num=n-pow(10,keta-1)+1
            a0=pow(10,keta-1)
            an=n
            csum=keta*num*(a0+an)//2
            res+=csum
            return res
        res%=MOD

# for i in range(20):
#     print(i,cnt(i))

l,r=map(int, input().split())
ans=cnt(r)-cnt(l-1)
print(ans%MOD)